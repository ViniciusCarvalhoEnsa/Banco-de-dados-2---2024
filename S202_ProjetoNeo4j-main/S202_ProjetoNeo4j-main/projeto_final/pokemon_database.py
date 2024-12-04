# ESSE ARQUIVO INTEIROOOOOOOOOOOOOOOOOOOOOOOOOO
from termcolor import colored

class PokemonDatabase:
    def __init__(self,database):
        self.db = database

    def open_packet(self):
        for i in range(5):
            query = """
                MATCH (p:Pokemon)
                RETURN p.name AS name
                ORDER BY rand()
                LIMIT 1
            """
            pokemon = self.db.execute_query(query)
            pokemon_found = pokemon[0]["name"]
            print(colored(f"[+] parabéns, você consegiu um {pokemon_found}!", "green"))
    
    def strongest_pokemon(self):
        query = """
            MATCH (p:Pokemon)
            WITH MAX(p.attack) AS max_attack
            MATCH (p:Pokemon) WHERE p.attack = max_attack
            RETURN p.name
        """
        result = self.db.execute_query(query)
        return result["p.name"]

    def count_pokemon(self):
        query = """
            MATCH (p:Pokemon)
            WITH COUNT(p) AS total_pokemons
            RETURN total_pokemons
        """
        result = self.db.execute_query(query)
        total_pokemons = result[0]["total_pokemons"]
        return int(total_pokemons)

    def count_byType(self,type):
        query = """
            MATCH (p:Pokemon)-[:IS_TYPE]->(t:Type {name: $type})
            WITH COUNT(p) AS total_pokemons_by_type
            RETURN total_pokemons_by_type
        """
        parameters = {"type": type}
        result = self.db.execute_query(query,parameters)
        return int(result["total_pokemons"])

    