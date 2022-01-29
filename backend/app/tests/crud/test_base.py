from app import crud


def test_get(db) -> None:

    query = "MATCH (p:Person) WHERE p.name = 'Emil' RETURN p;"
    results = crud.base_test.get(db=db,
                                 query=query)

    assert results == 0
