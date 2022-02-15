from neo4j import GraphDatabase


class CRUDBase:
    def __init__(self):
        pass

    def get(self, db: GraphDatabase, label: str, name: str) -> list:
        query = f"MATCH (node:{label}) WHERE node.name='{name}' RETURN node"
        result = db.run(query)
        return [record.data() for record in result]

    def create(self, db: GraphDatabase, label: str, name: str) -> list:
        query = f"CREATE (node:{label} {{name: '{name}'}}) RETURN node"
        result = db.run(query)
        return [record.data() for record in result]

    def delete(self, db: GraphDatabase, label: str, name: str) -> list:
        query = f"MATCH(node: {label} {{name: '{name}'}}) DELETE node RETURN node"
        result = db.run(query)
        return [record.data() for record in result]
