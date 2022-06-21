from uuid import uuid4

from neo4j import GraphDatabase

from app.core.security import get_password_hash, verify_password
from app.core.config import settings
from app.crud.base import Base
from app.libs.converter import ModelConverter
from app import models


def check_rowdata(model, rowdata) -> dict:
    if not rowdata:
        return None
    elif len(rowdata) == 1:
        return model(**rowdata[0])
    else:
        raise ValueError(
            "Multiple users with the same email address or id exist")


class CRUDUser(Base):

    def __init__(self):
        pass

    def get_by_email(self, db: GraphDatabase, email: str) -> list:
        query = f"""
            MATCH ({settings.USER_NODE_NAME}:{settings.USER_NODE_LABEL} {{email: '{email}'}})
            RETURN {settings.USER_NODE_NAME}
        """
        result = db.run(query)
        user = [record.get(settings.USER_NODE_NAME)
                for record in result.data()]
        return check_rowdata(models.User, user)

    def get_by_uuid(self, db, id):
        query = f"""
            MATCH ({settings.USER_NODE_NAME}:{settings.USER_NODE_LABEL} {{id: '{id}'}})
            RETURN {settings.USER_NODE_NAME}
        """
        result = db.run(query)
        user = [record.get(settings.USER_NODE_NAME)
                for record in result.data()]

        return check_rowdata(models.User, user)

    def create(
            self,
            db: GraphDatabase,
            email: str,
            password: str) -> list:

        user = models.User(
            id=uuid4().hex,
            email=email,
            hashed_password=get_password_hash(password),
            is_superuser=True)
        query = f"""
                CREATE ({settings.USER_NODE_NAME}:{settings.USER_NODE_LABEL}
                        {ModelConverter.to_cypher_object(user)})
                RETURN {settings.USER_NODE_NAME}
                """
        result = db.run(query)
        user = [record.get(settings.USER_NODE_NAME)
                for record in result.data()]

        return check_rowdata(models.User, user)

    def update(self,
               db: GraphDatabase,
               id: str,
               data: dict) -> list:
        query = f"""
                MATCH ({settings.USER_NODE_NAME}:{settings.USER_NODE_LABEL})
                WHERE {settings.USER_NODE_NAME}.id='{id}'
                SET {settings.USER_NODE_NAME} = {ModelConverter.to_cypher_object(models.User(**data))}
                RETURN {settings.USER_NODE_NAME}
                """
        result = db.run(query)
        user = [record.get(settings.USER_NODE_NAME)
                for record in result.data()]

        return check_rowdata(models.User, user)

    def delete(
            self,
            db: GraphDatabase,
            id: str) -> None:
        query = f"""
                MATCH({settings.USER_NODE_NAME}:{settings.USER_NODE_LABEL})
                WHERE {settings.USER_NODE_NAME}.id='{id}'
                DELETE {settings.USER_NODE_NAME}
                """
        db.run(query)

    def delete_by_email(
            self,
            db: GraphDatabase,
            email: str) -> None:
        query = f"""
                MATCH({settings.USER_NODE_NAME}:{settings.USER_NODE_LABEL})
                WHERE {settings.USER_NODE_NAME}.email='{email}'
                DELETE {settings.USER_NODE_NAME}
                """
        db.run(query)

    def authenticate(
            self,
            db: GraphDatabase,
            email: str,
            password: str) -> list:
        user = self.get_by_email(db, email=email)

        if not user:
            return None
        else:
            if not verify_password(password, user.hashed_password):
                return None
            return user

    def is_active(self, user: models.User) -> bool:
        return user.is_active

    def is_superuser(self, user: models.User) -> bool:
        return user.is_superuser


user = CRUDUser()
