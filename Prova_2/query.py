from neo4j import GraphDatabase

class Database:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def execute_query(self, query, parameters=None):
        data = []
        with self.driver.session() as session:
            results = session.run(query, parameters)
            for record in results:
                data.append(record)
            return data
        
    def drop_all(self):
        with self.driver.session() as session:
            session.run("MATCH (n) DETACH DELETE n")    

db = Database("")

#-------------------------------------------------------------------------------------------------------- Questão 01
result = db.query("MATCH (t:Teacher {name: 'Renzo'}) RETURN t.ano_nasc, t.cpf")
print(result)

result = db.query("MATCH (t:Teacher) WHERE t.name STARTS WITH 'M' RETURN t.name, t.cpf")
print(result)

result = db.query("MATCH (c:City) RETURN c.name")
print(result)

result = db.query("MATCH (s:School) WHERE s.number >= 150 AND s.number <= 550 RETURN s.name, s.address, s.number")
print(result)

#-------------------------------------------------------------------------------------------------------- Questão 02
result = db.query("MATCH (t:Teacher) RETURN MIN(t.ano_nasc) AS MaisVelho, MAX(t.ano_nasc) AS MaisJovem")
print(result)

result = db.query("MATCH (c:City) RETURN AVG(c.population) AS MediaPopulacao")
print(result)

result = db.query("MATCH (c:City {cep: '37540-000'}) RETURN REPLACE(c.name, 'a', 'A')")
print(result)

result = db.query("MATCH (t:Teacher) RETURN SUBSTRING(t.name, 2, 1)")
print(result)

db.close()