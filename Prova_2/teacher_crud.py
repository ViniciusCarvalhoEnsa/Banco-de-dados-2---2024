from neo4j import GraphDatabase

class Database:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def query(self, query, parameters=None):
        with self.driver.session() as session:
            return list(session.run(query, parameters))

class TeacherCRUD:
    def __init__(self, db):
        self.db = db

    def create(self, name, ano_nasc, cpf):
        query = "CREATE (:Teacher {name: $name, ano_nasc: $ano_nasc, cpf: $cpf})"
        self.db.query(query, parameters={"name": name, "ano_nasc": ano_nasc, "cpf": cpf})

    def read(self, name):
        query = "MATCH (t:Teacher {name: $name}) RETURN t"
        result = self.db.query(query, parameters={"name": name})
        return result

    def delete(self, name):
        query = "MATCH (t:Teacher {name: $name}) DELETE t"
        self.db.query(query, parameters={"name": name})

    def update(self, name, new_cpf):
        query = "MATCH (t:Teacher {name: $name}) SET t.cpf = $new_cpf"
        self.db.query(query, parameters={"name": name, "new_cpf": new_cpf})