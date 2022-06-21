from neo4j import GraphDatabase

from app.core.config import settings
from app.libs.converter import ModelConverter


class Base:

    def __init__(self):
        pass

    def get(self, db: GraphDatabase, node_name, node_label, id: str) -> list:
        query = f"""
            MATCH ({node_name}:{node_label} {{id: '{id}'}})
            RETURN {node_name}
        """
        result = db.run(query)
        return [record.get(node_name)
                for record in result.data()]

    def create(
            self,
            db: GraphDatabase,
            node_name,
            node_label,
            data: object) -> list:
        query = f"""
                CREATE ({node_name}:{node_label}
                        {ModelConverter.to_cypher_object(data)})
                RETURN {node_name}
                """
        result = db.run(query)
        return [record.get(node_name)
                for record in result.data()]

    def update(self,
               db: GraphDatabase, node_name, node_label,
               id: str,
               data: object) -> list:
        query = f"""
                MATCH ({node_name}:{node_label})
                WHERE {node_name}.id='{id}'
                SET {node_name} = {ModelConverter.to_cypher_object(data)}
                RETURN {node_name}
                """
        result = db.run(query)
        return [record.get(node_name)
                for record in result.data()]

    def delete(
            self,
            db: GraphDatabase,
            node_name,
            node_label,
            id: str) -> None:
        query = f"""
                MATCH({node_name}:{node_label})
                WHERE {node_name}.id='{id}'
                DELETE {node_name}
                """
        db.run(query)


base = Base()
