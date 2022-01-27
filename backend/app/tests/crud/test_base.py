

def test_get(db) -> None:
    q1 = "MATCH (n:Person {name:'Emil'}) RETURN n"
    nodes = db.run(q1)
    results = [record for record in nodes.data()]

    assert results == 0
