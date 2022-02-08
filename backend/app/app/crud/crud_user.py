from app.crud.base import CRUDBase
from neo4j import GraphDatabase


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
                            hashed_password: '{hashed_password}'
                            is_active: '{is_active}'

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


user = CRUDUser()
