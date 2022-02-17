from secrets import token_bytes
from app.api.deps import get_current_user
from app.core.security import create_access_token
from app import crud


def test_get_current_user(db):

    label = "test"
    email = "naoki@dummy.com"
    password = "password"

    result = crud.user.create(db=db,
                              label=label,
                              email=email,
                              password=password)

    token = create_access_token(result[0]["node"]["id"])
    user = get_current_user(
        db=db,
        token=token)

    crud.user.delete_by_email(db=db,
                              label=label,
                              email=email)

    assert user["node"]["id"] == result[0]["node"]["id"]
    assert user["node"]["email"] == email
