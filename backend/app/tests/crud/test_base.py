from app import crud


def test_create(db) -> None:

    label = "test"
    key = "name"
    value = "naoki"

    properties = {
        key: value
    }
    results = crud.base_test.create(db=db,
                                    label=label,
                                    properties=properties)

    assert results == 0


def test_get(db) -> None:

    label = "test"
    key = "name"
    value = "naoki"

    results = crud.base_test.get(db=db,
                                 label=label,
                                 key=key,
                                 value=value)

    assert results == 0
