from app.core.security import (create_access_token,
                               verify_password,
                               get_password_hash)

password = "password"


def test_get_password_hash_and_verify_password():
    hashed_pass = get_password_hash(password)

    assert isinstance(hashed_pass, str)
    assert verify_password(
        password,
        hashed_pass)


def test_create_access_token():
    ressult = create_access_token({"user": "user", "password": password})

    assert ressult == 0
