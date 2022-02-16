from neo4j import GraphDatabase

from typing import Any, Dict, Optional, Union
from app.core.security import get_password_hash, verify_password
from app.models.user import User
from app.crud.base import CRUDBase


class CRUDUser(CRUDBase):
    def get_by_email(self, db: GraphDatabase, label: str, email: str) -> list:
        query = f"MATCH (node:{label}) WHERE node.email='{email}' RETURN node"
        result = db.run(query)
        return [record.data() for record in result]

    def get_by_uuid(self, db: GraphDatabase, label: str, uuid: str) -> list:
        query = f"MATCH (node:{label}) WHERE node.uuid='{uuid}' RETURN node"
        result = db.run(query)
        return [record.data() for record in result]

    def create(self, db: GraphDatabase, label: str, uuid: str, email: str) -> list:
        query = f"""
                CREATE (node:{label}
                        {{
                            uuid: '{uuid}',
                            email: '{email}'
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
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    def is_active(self, user: User) -> bool:
        return user.is_active

    def is_superuser(self, user: User) -> bool:
        return user.is_superuser


user = CRUDUser()
