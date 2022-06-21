import redis

from neo4j import GraphDatabase
from app.core.config import settings

neo4j_driver = GraphDatabase.driver(
    f"neo4j://{settings.GRAPH_DB_HOST}:{settings.GRAPH_DB_PORT}",
    auth=(settings.GRAPH_DB_USER,
          settings.GRAPH_DB_PASSWORD))
SessionLocal = neo4j_driver.session()


def get_db() -> GraphDatabase:
    try:
        db = SessionLocal
        yield db
    finally:
        db.close()


redis_connection = redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=settings.REDIS_DB_NUM)


def get_cache() -> redis:
    yield redis_connection
