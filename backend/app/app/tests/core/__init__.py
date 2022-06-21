import base64
import json

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

    header_base64 = ressult.split(".")[0]
    payload_base64 = ressult.split(".")[1]

    if len(header_base64) % 4 != 0:
        header_base64 += "=" * (4 - len(payload_base64) % 4)
    if len(payload_base64) % 4 != 0:
        payload_base64 += "=" * (4 - len(payload_base64) % 4)

    HEADER = json.loads(base64.b64decode(header_base64).decode())
    PAYLOAD = json.loads(base64.b64decode(payload_base64).decode())

    assert HEADER == {"alg": "HS256", "typ": "JWT"}
    assert PAYLOAD["sub"] == f"{{'user': 'user', 'password': '{password}'}}"
