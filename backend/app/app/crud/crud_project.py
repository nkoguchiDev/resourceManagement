from uuid import uuid4

from neo4j import GraphDatabase

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


class CRUDProject(Base):

    def __init__(self):
        self._NODE_NAME = "project"
        self._NODE_LABEL = "Project"

    def create(
            self,
            db: GraphDatabase,
            name: str,
            description: str = None) -> list:

        project = models.Project(
            id=uuid4().hex,
            name=name,
            description=description)
        query = f"""
                CREATE ({self._NODE_NAME}:{self._NODE_LABEL}
                        {ModelConverter.to_cypher_object(project)})
                RETURN {self._NODE_NAME}
                """
        result = db.run(query)
        user = [record.get(self._NODE_NAME)
                for record in result.data()]

        return check_rowdata(models.User, user)

    def delete_by_id(
            self,
            db: GraphDatabase,
            id: str) -> None:
        query = f"""
                MATCH({self._NODE_NAME}:{self._NODE_LABEL})
                WHERE {self._NODE_NAME}.id='{id}'
                DELETE {self._NODE_NAME}
                """
        db.run(query)


project = CRUDProject()
