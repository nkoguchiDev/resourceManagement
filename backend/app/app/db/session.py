from neo4j import GraphDatabase

from app.core.config import settings

driver = GraphDatabase.driver(settings.NEO4J_DATABASE_URI,
                              auth=(settings.NEO4J_USERNAME,
                                    settings.NEO4J_PASSWORD))
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
