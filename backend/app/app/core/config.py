from pydantic import BaseSettings


class Settings(BaseSettings):
    # project settings
    PROJECT_NAME: str = "IAM"
    API_V1_STR: str = "/api/v1"

    SECRET_KEY: str
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 8

    # neo4j server settings
    GRAPH_DB_USER: str
    GRAPH_DB_PASSWORD: str
    GRAPH_DB_HOST: str
    GRAPH_DB_PORT: int

    # cypher query settings
    USER_NODE_NAME: str = "user"
    USER_NODE_LABEL: str = "User"
    TOKEN_NODE_NAME: str = "token"
    TOKEN_NODE_LABEL: str = "Token"

    # redis settings
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_DB_NUM: int = 0

    class Config:
        env_file = 'local.env'


settings = Settings()
