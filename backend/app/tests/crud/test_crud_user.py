from app import crud
from app.core.security import verify_password


def test_create(db) -> None:

    label = "test"
    email = "naoki@dummy.com"
    password = "password"

    results = crud.user.create(db=db,
                               label=label,
                               email=email,
                               password=password)

    assert verify_password(password, results[0]["node"]["hashed_password"])
    assert results[0]["node"]["email"] == email


def test_get_by_email(db) -> None:

    label = "test"
    email = "naoki@dummy.com"

    results = crud.user.get_by_email(db=db,
                                     label=label,
                                     email=email)

    assert results[0]["node"]["email"] == email


def test_delete_by_email(db) -> None:

    label = "test"
    email = "naoki@dummy.com"

    results = crud.user.delete_by_email(db=db,
                                        label=label,
                                        email=email)

    assert results[0]["node"] == {}


def test_authenticate(db) -> None:

    label = "test"
    email = "naoki@dummy.com"
    password = "password"

    crud.user.create(db=db,
                     label=label,
                     email=email,
                     password=password)

    results = crud.user.authenticate(
        db,
        email=email,
        password=password)

    crud.user.delete_by_email(db=db,
                              label=label,
                              email=email)

    assert results.email == email
