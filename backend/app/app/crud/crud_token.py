import redis

from app.core.config import settings
from app import models
from app.libs.converter import ModelConverter


class CRUDToken:
    def __init__(self) -> None:
        pass

    def create(
            self,
            cache: redis,
            key: str,
            data: dict) -> list:
        return cache.hset(key, mapping=models.OauthToken(**data).dict(exclude_none=True))

    def get(
            self,
            cache: redis,
            key: str) -> list:
        return ModelConverter.byte_key_value_to_dict(cache.hgetall(key))

    def delete(
            self,
            cache: redis,
            key: str) -> list:
        return cache.delete(key)


token = CRUDToken()
