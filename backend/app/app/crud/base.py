from neo4j import GraphDatabase


class CRUDBase:
    def __init__(self):
        pass

    def get(self, db: GraphDatabase, label: str, key: str, value: str) -> None:
        query = f"MATCH (node:{label}) WHERE node.{key}='{value}' RETURN node"
        nodes = []
        result = db.run(query)
        for record in result:
            nodes.append(record)
        return nodes

    def create(self, db: GraphDatabase, label: str, properties: dict) -> None:
        query = f"CREATE (node:{label} {properties})"
        nodes = []
        result = db.run(query)
        for record in result:
            nodes.append(record)
        return nodes


base_test = CRUDBase()
