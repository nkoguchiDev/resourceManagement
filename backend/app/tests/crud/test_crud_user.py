from app import crud
from app.core.security import verify_password


def test_create(db) -> None:

    email = "naoki@dummy.com"
    password = "password"

    user = crud.user.create(db=db,
                            email=email,
                            password=password)

    assert verify_password(password, user.hashed_password)
    assert user.email == email


def test_get_by_email(db) -> None:

    email = "naoki@dummy.com"

    user = crud.user.get_by_email(db=db,
                                  email=email)

    assert user.email == email


def test_delete_by_email(db) -> None:

    email = "naoki@dummy.com"

    user = crud.user.delete_by_email(db=db,
                                     email=email)

    assert user is None


def test_authenticate(db) -> None:

    email = "naoki@dummy.com"
    password = "password"

    crud.user.create(db=db,
                     email=email,
                     password=password)

    results = crud.user.authenticate(
        db,
        email=email,
        password=password)

    crud.user.delete_by_email(db=db,
                              email=email)

    assert results.email == email
