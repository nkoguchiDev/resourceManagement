import uuid


from app import crud

token = uuid.uuid4().hex

data = {
    "developerId": uuid.uuid4().hex,
}


class TestCRUDClientCredential:

    def test_create(self, redis_cache):
        assert crud.token.create(redis_cache, token, data)

    def test_get(self, redis_cache):
        result = crud.token.get(redis_cache, token)

        assert result["developerId"] == data["developerId"]

    def test_delete(self, redis_cache):

        assert crud.token.delete(redis_cache, token)
