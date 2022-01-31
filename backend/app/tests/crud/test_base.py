from app import crud


def test_create(db) -> None:

    label = "test"
    name = "naoki"

    results = crud.base_test.create(db=db,
                                    label=label,
                                    name=name)

    assert results == 0


def test_get(db) -> None:

    label = "test"
    name = "naoki"

    results = crud.base_test.get(db=db,
                                 label=label,
                                 name=name)

    assert results == 0


def test_delete(db) -> None:

    label = "test"
    name = "naoki"

    results = crud.base_test.delete(db=db,
                                    label=label,
                                    name=name)

    assert results == 0
