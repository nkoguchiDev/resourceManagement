from app.crud.base import CRUDBase


def test_create(db) -> None:

    label = "test"
    name = "naoki"

    crud = CRUDBase()

    results = crud.create(db=db,
                          label=label,
                          name=name)

    assert results[0]["node"] == {'name': name}


def test_get(db) -> None:

    label = "test"
    name = "naoki"

    crud = CRUDBase()

    results = crud.get(db=db,
                       label=label,
                       name=name)

    assert results[0]["node"] == {'name': name}


def test_delete(db) -> None:

    label = "test"
    name = "naoki"

    crud = CRUDBase()

    results = crud.delete(db=db,
                          label=label,
                          name=name)

    assert results[0]["node"] == {}
