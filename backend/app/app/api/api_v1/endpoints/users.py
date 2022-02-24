from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from neo4j import GraphDatabase

from app import crud, models, schemas
from app.api import deps
from app.core.config import settings

router = APIRouter()


@router.post("/open", response_model=schemas.User)
def create_user_open(
    *,
    db: GraphDatabase = Depends(deps.get_db),
    password: str = Body(...),
    email: EmailStr = Body(...),
    full_name: str = Body(None),
) -> Any:
    """
    Create new user without the need to be logged in.
    """
    if not settings.USERS_OPEN_REGISTRATION:
        raise HTTPException(
            status_code=403,
            detail="Open user registration is forbidden on this server",
        )
    user = crud.user.get_by_email(db, email=email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system",
        )
    # user_in = schemas.UserCreate(
    #     password=password,
    #     email=email,
    #     full_name=full_name,
    #     is_superuser=True)
    # user = crud.user.create(db, obj_in=user_in)
    user = crud.user.create(db, password=password,
                            email=email,
                            full_name=full_name,
                            is_superuser=True)
    return user
