import uuid


from app import crud


data = {
    "id": uuid.uuid4().hex,
    "key": uuid.uuid4().hex,
    "secret": uuid.uuid4().hex,
}


class TestCRUDClientCredential:

    def test_create(self, db):
        result = crud.client_credential.create(db, data)
        assert result[0]['key'] == data['key']
        assert result[0]['secret'] == data['secret']

    def test_delete(self, db):
        crud.client_credential.delete(db, id=data["id"])
        result = crud.client_credential.get(db, id=data["id"])

        assert len(result) == 0
