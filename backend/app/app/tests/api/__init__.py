from app.api.deps import get_current_user
from app.core.security import create_access_token
from app import crud


def test_get_current_user(db):

    email = "naoki@dummy.com"
    password = "password"

    result = crud.user.create(db=db,
                              email=email,
                              password=password)

    token = create_access_token(result.id)
    user = get_current_user(
        db=db,
        token=token)

    crud.user.delete_by_email(db=db,
                              email=email)

    assert user.id == result.id
    assert user.email == email
