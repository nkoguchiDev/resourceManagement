from app.api.deps import get_current_user


def test_get_current_user():
    user = get_current_user(
        token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDU2MzQ1NjksInN1YiI6InsndXNlcic6ICd1c2VyJywgJ3Bhc3N3b3JkJzogJ3Bhc3N3b3JkJ30ifQ.8pzgB5y7b5urdekf56MNmiyAX1YZbw6RxusHtQDdtZM")
    assert user.username == 'user'
    assert user.password == 'password'
