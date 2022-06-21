import redis

from app.db.session import SessionLocal, redis_connection

from neo4j import GraphDatabase

import pytest


@pytest.fixture(scope="session")
def db() -> GraphDatabase:
    yield SessionLocal


@pytest.fixture(scope="session")
def redis_cache() -> redis:
    yield redis_connection
