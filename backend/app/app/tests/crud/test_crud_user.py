

from app import crud
from app.tests.utils.generator import random_str


email = random_str(7) + '@gmail.com'
password = random_str(7)


class TestCRUDUser:

    def test_create(self, db):
        result = crud.user.create(db=db,
                                  email=email,
                                  password=password)
        assert result.email == email

    def test_get_by_email(self, db):
        result = crud.user.get_by_email(db, email=email)

        assert result.email == email

    def test_authenticate(self, db):
        result = crud.user.authenticate(db, email=email, password=password)

        assert result.email == email

    def test_authenticate_faild(self, db):
        result = crud.user.authenticate(db, email=email, password="dummy")

        assert result is None

    def test_is_active(self, db):
        result = crud.user.authenticate(db, email=email, password=password)
        result = crud.user.is_active(user=result)

        assert result is True

    def test_is_superuser(self, db):
        result = crud.user.authenticate(db, email=email, password=password)
        result = crud.user.is_superuser(user=result)

        assert result is True

    # def test_delete(self, db):
    #     crud.user.delete(db, id=_user["id"])
    #     result = crud.user.get(db, id=email)

    #     assert len(result) == 0
