from datetime import timedelta
from typing import Any

from fastapi import APIRouter, Depends
from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from neo4j import GraphDatabase

from app import models, schemas
from app import crud, models, schemas
from app.api import deps
from app.core import security
# from app.core.config import settings
from app.core.security import get_password_hash
# from app.utils import (
#     generate_password_reset_token,
#     send_reset_password_email,
#     verify_password_reset_token,
# )

router = APIRouter()


class settings:
    ACCESS_TOKEN_EXPIRE_MINUTES = timedelta(minutes=5)


@router.post("/login/access-token", response_model=schemas.Token)
def login_access_token(db: GraphDatabase = Depends(deps.get_db),
                       form_data: OAuth2PasswordRequestForm = Depends()) -> Any:
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    user = crud.user.authenticate(
        db, email=form_data.username, password=form_data.password
    )
    if not user:
        raise HTTPException(
            status_code=400,
            detail="Incorrect email or password")
    elif not crud.user.is_active(user):
        raise HTTPException(status_code=400, detail="Inactive user")
    access_token_expires = timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": security.create_access_token(
            user.id, expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }
