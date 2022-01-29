from app.db.session import SessionLocal

from neo4j import GraphDatabase

import pytest


@pytest.fixture(scope="session")
def db() -> GraphDatabase:
    yield SessionLocal
