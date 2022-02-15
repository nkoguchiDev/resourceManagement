from app import crud


def test_create(db) -> None:

    label = "test"
    uuid = "uuid0001"
    email = "naoki@dummy.com"

    results = crud.user.create(db=db,
                               label=label,
                               uuid=uuid,
                               email=email)

    assert results[0]["node"]["uuid"] == uuid
    assert results[0]["node"]["email"] == email


def test_get_by_uuid(db) -> None:

    label = "test"
    uuid = "uuid0001"
    email = "naoki@dummy.com"

    results = crud.user.get_by_uuid(db=db,
                                    label=label,
                                    uuid=uuid)

    assert results[0]["node"]["uuid"] == uuid
    assert results[0]["node"]["email"] == email


def test_delete_by_uuid(db) -> None:

    label = "test"
    uuid = "uuid0001"

    results = crud.user.delete_by_uuid(db=db,
                                       label=label,
                                       uuid=uuid)

    assert results[0]["node"] == {}
