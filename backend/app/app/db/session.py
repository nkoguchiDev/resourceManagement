from neo4j import GraphDatabase
from app.core.config import settings

driver = GraphDatabase.driver(
    f"neo4j://{settings.GRAPH_DB_HOST}:{settings.GRAPH_DB_PORT}",
    auth=(settings.GRAPH_DB_USER,
          settings.GRAPH_DB_PASSWORD))
SessionLocal = driver.session()
