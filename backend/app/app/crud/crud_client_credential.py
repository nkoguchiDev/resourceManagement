from neo4j import GraphDatabase

from app.core.config import settings
from app.crud.base import Base
from app.libs.converter import ModelConverter
from app import models


class CRUDClientCredential(Base):

    def __init__(self):
        pass

    def get(self, db: GraphDatabase, id: str) -> list:
        query = f"""
            MATCH ({settings.TOKEN_NODE_NAME}:{settings.TOKEN_NODE_LABEL} {{id: '{id}'}})
            RETURN {settings.TOKEN_NODE_NAME}
        """
        result = db.run(query)
        return [record.get(settings.TOKEN_NODE_NAME)
                for record in result.data()]

    def create(
            self,
            db: GraphDatabase,
            data: dict) -> list:
        query = f"""
                CREATE ({settings.TOKEN_NODE_NAME}:{settings.TOKEN_NODE_LABEL}
                        {ModelConverter.to_cypher_object(models.ClientCredential(**data))})
                RETURN {settings.TOKEN_NODE_NAME}
                """
        result = db.run(query)
        return [record.get(settings.TOKEN_NODE_NAME)
                for record in result.data()]

#     def update(self,
#                db: GraphDatabase,
#                id: str,
#                data: dict) -> list:
#         query = f"""
#                 MATCH ({settings.TOKEN_NODE_NAME}:{settings.TOKEN_NODE_LABEL})
#                 WHERE {settings.TOKEN_NODE_NAME}.id='{id}'
#                 SET {settings.TOKEN_NODE_NAME} = {ModelConverter.to_cypher_object(ClientCredential(**data))}
#                 RETURN {settings.TOKEN_NODE_NAME}
#                 """
#         result = db.run(query)
#         return [record.get(settings.TOKEN_NODE_NAME)
#                 for record in result.data()]

    def delete(
            self,
            db: GraphDatabase,
            id: str) -> None:
        query = f"""
                MATCH({settings.TOKEN_NODE_NAME}:{settings.TOKEN_NODE_LABEL})
                WHERE {settings.TOKEN_NODE_NAME}.id='{id}'
                DELETE {settings.TOKEN_NODE_NAME}
                """
        db.run(query)


client_credential = CRUDClientCredential()
