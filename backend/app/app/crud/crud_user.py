import uuid

from neo4j import GraphDatabase

from typing import Any, Dict, List, Optional, Union

from app.core.security import get_password_hash, verify_password
from app.core.config import settings

from app.models.user import User
from app.crud.base import CRUDBase


def check_rowdata(rowdata) -> dict:
    if not rowdata:
        return None
    elif len(rowdata) == 1:
        return rowdata[0][settings.USER_NODE_NAME]
    else:
        raise ValueError("Multiple users with the same email address or id exist")


class CRUDUser(CRUDBase):
    def get_by_email(self, db: GraphDatabase, email: str) -> list:
        query = f"""
        MATCH ({settings.USER_NODE_NAME}:{settings.USER_NODE_LABEL})
        WHERE {settings.USER_NODE_NAME}.email='{email}'
        RETURN {settings.USER_NODE_NAME}
        """
        result = db.run(query)
        user = check_rowdata([record.data() for record in result])
        if not user:
            return None
        else:
            return User(**user)

    def get_by_uuid(self, db: GraphDatabase, id: str) -> list:
        query = f"""
        MATCH ({settings.USER_NODE_NAME}:{settings.USER_NODE_LABEL})
        WHERE {settings.USER_NODE_NAME}.id='{id}'
        RETURN {settings.USER_NODE_NAME}
        """
        result = db.run(query)
        user = check_rowdata([record.data() for record in result])
        if not user:
            return None
        else:
            return User(**user)

    def create(
            self,
            db: GraphDatabase,
            email: str,
            password: str,
            full_name: str = None,
            is_active: bool = True,
            is_superuser: bool = False) -> list:
        query = f"""
                CREATE ({settings.USER_NODE_NAME}:{settings.USER_NODE_LABEL}
                        {{
                            id: '{uuid.uuid4()}',
                            email: '{email}',
                            hashed_password: '{get_password_hash(password)}',
                            full_name: '{full_name}',
                            is_active: {is_active},
                            is_superuser: {is_superuser}
                        }}
                        )
                        RETURN {settings.USER_NODE_NAME}
                """
        result = db.run(query)
        user = check_rowdata([record.data() for record in result])
        if not user:
            return None
        else:
            return User(**user)

    def delete_by_email(self, db: GraphDatabase, email: str) -> list:
        query = f"""
        MATCH({settings.USER_NODE_NAME}:{settings.USER_NODE_LABEL}
            {{
                email: '{email}'
            }}
        )
        DELETE {settings.USER_NODE_NAME}
        RETURN {settings.USER_NODE_NAME}
        """
        result = db.run(query)
        user = check_rowdata([record.data() for record in result])
        if not user:
            return None
        else:
            return User(**user)

    def delete_by_uuid(self, db: GraphDatabase, uuid: str) -> list:
        query = f"""
        MATCH({settings.USER_NODE_NAME}:{settings.USER_NODE_NAME}
            {{
                uuid: '{uuid}'
            }}
        )
        DELETE {settings.USER_NODE_NAME}
        RETURN {settings.USER_NODE_NAME}
        """
        result = db.run(query)
        user = check_rowdata([record.data() for record in result])
        if not user:
            return None
        else:
            return User(**user)

    def authenticate(
            self,
            db: GraphDatabase,
            *,
            email: str,
            password: str) -> Optional[User]:
        user = self.get_by_email(db, email=email)
        if not user:
            return None
        else:
            if not verify_password(password, user.hashed_password):
                return None
            return user

    def is_active(self, user: User) -> bool:
        return user.is_active

    def is_superuser(self, user: User) -> bool:
        return user.is_superuser


user = CRUDUser()
