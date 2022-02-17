import uuid

from neo4j import GraphDatabase

from typing import Any, Dict, List, Optional, Union
from app.core.security import get_password_hash, verify_password
from app.models.user import User
from app.crud.base import CRUDBase


def check_rowdata(rowdata) -> dict:
    if not rowdata:
        return None
    elif len(rowdata) == 1:
        return rowdata[0]["node"]
    else:
        raise ValueError("Multiple users with the same email address exist")


class CRUDUser(CRUDBase):
    def get_by_email(self, db: GraphDatabase, label: str, email: str) -> list:
        query = f"MATCH (node:{label}) WHERE node.email='{email}' RETURN node"
        result = db.run(query)
        return [record.data() for record in result]

    def get_by_uuid(self, db: GraphDatabase, label: str, id: str) -> list:
        query = f"MATCH (node:{label}) WHERE node.id='{id}' RETURN node"
        result = db.run(query)
        return [record.data() for record in result]

    def create(self, db: GraphDatabase, label: str, email: str, password: str) -> list:
        query = f"""
                CREATE (node:{label}
                        {{
                            id: '{uuid.uuid4()}',
                            email: '{email}',
                            hashed_password: '{get_password_hash(password)}'
                        }}
                        ) RETURN node
                """
        result = db.run(query)
        return [record.data() for record in result]

    def delete_by_email(self, db: GraphDatabase, label: str, email: str) -> list:
        query = f"MATCH(node: {label} {{email: '{email}'}}) DELETE node RETURN node"
        result = db.run(query)
        return [record.data() for record in result]

    def delete_by_uuid(self, db: GraphDatabase, label: str, uuid: str) -> list:
        query = f"MATCH(node: {label} {{uuid: '{uuid}'}}) DELETE node RETURN node"
        result = db.run(query)
        return [record.data() for record in result]

    def authenticate(
            self,
            db: GraphDatabase,
            *,
            email: str,
            password: str) -> Optional[User]:
        user = self.get_by_email(db, label="test", email=email)
        user = check_rowdata(user)
        if not user:
            return None
        else:
            if not verify_password(password, user["hashed_password"]):
                return None
            return User(**user)

    def is_active(self, user: User) -> bool:
        return user.is_active

    def is_superuser(self, user: User) -> bool:
        return user.is_superuser


user = CRUDUser()
