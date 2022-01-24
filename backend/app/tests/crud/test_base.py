from app import crud


def test_get(db) -> None:
    a = crud.base.get(db)
    assert a == 0
