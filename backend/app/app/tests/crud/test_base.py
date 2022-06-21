import uuid


from pydantic import BaseModel

from app import crud
from app.tests.utils.generator import random_str


class User(BaseModel):
    id: str
    name: str = None
    email: str = None
    description: str = None
    price: str = None
    tax: str = None


_user = {
    "id": uuid.uuid4().hex,
    "name": random_str(7),
    "email": random_str(7) + '@gmail.com',
    "description": 'description1',
    "price": 'price2',
    "tax": 'tax3'
}

node_name = "node"
node_label = "label"


class TestCRUDBase:

    def test_create(self, db):
        result = crud.base.create(db, node_name, node_label, User(**_user))
        assert result[0]['name'] == _user['name']

    def test_get(self, db):
        result = crud.base.get(db, node_name, node_label, id=_user["id"])

        assert len(result) == 1
        assert result[0]['email'] == _user['email']

    def test_update(self, db):
        update_email = random_str(7) + '@gmail.com'
        result = crud.base.update(db, node_name, node_label, id=_user["id"], data=User(
            **{"id": _user["id"], "email": update_email}))

        assert len(result) == 1
        assert result[0]['email'] == update_email

    def test_delete(self, db):
        crud.base.delete(db, node_name, node_label, id=_user["id"])
        result = crud.base.get(db, node_name, node_label, id=_user["id"])

        assert len(result) == 0
