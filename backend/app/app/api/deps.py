from typing import Generator

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError
from neo4j import GraphDatabase

from app import crud, models, schemas
from app.core import security
# from app.core.config import settings
from app.db.session import SessionLocal

reusable_oauth2 = OAuth2PasswordBearer(
    # tokenUrl=f"{settings.API_V1_STR}/login/access-token"
    tokenUrl="/v1/api/login/access-token"
)


class settings:
    SECRET_KEY = "cce45e4c8450c2781ff1f2e1436cd61fb49c730f5b74b7b4824ca09d77eb89c3"


def get_db() -> Generator:
    try:
        db = SessionLocal
        yield db
    finally:
        db.close()


def get_current_user(
    db: GraphDatabase = Depends(get_db), token: str = Depends(reusable_oauth2)
) -> models.User:
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[security.ALGORITHM]
        )
        token_data = schemas.TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    user = crud.user.get_by_uuid(db, label="test", id=token_data.sub)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    elif len(user) > 1:
        raise HTTPException(status_code=400, detail="Multiple users found")
    else:
        return user[0]


def get_current_active_user(
    current_user: models.User = Depends(get_current_user),
) -> models.User:
    if not crud.user.is_active(current_user):
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


def get_current_active_superuser(
    current_user: models.User = Depends(get_current_user),
) -> models.User:
    if not crud.user.is_superuser(current_user):
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return current_user
