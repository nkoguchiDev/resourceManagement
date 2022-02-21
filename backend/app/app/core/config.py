from typing import Any, Dict, List, Optional, Union
from pydantic import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 8

    # graph database settings
    GRAPH_DB_HOST: str
    GRAPH_DB_PORT: int
    GRAPH_DB_USER: str
    GRAPH_DB_PASSWORD: str

    USER_NODE_NAME: str = "User"
    USER_NODE_LABEL: str = "User"

    PROJECT_NAME: str = "resourceManager"
    API_V1_STR: str = "/api/v1"

    class Config:
        env_file = 'local.env'


settings = Settings()
