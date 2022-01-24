from neo4j import GraphDatabase


class CRUDBase:
    def __init__(self):
        pass

    def get(self, db: GraphDatabase, id) -> None:
        nodes = []
        query = "MATCH(n) return n"
        result = db.run(query)
        for record in result:
            nodes.append(record)
        return nodes
