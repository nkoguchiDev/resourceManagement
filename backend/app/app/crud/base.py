from neo4j import GraphDatabase


class CRUDBase:
    def __init__(self):
        pass

    def get(self, db: GraphDatabase, query: str) -> None:
        nodes = []
        result = db.run(query)
        for record in result:
            nodes.append(record)
        return nodes


base_test = CRUDBase()
