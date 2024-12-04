from termcolor import colored
class PokemonMODEL:
    def __init__(self,database):
        self.db = database
    
    def create_pokemon(self,name,type,evolution,total,hp,attack):
        query = """
            CREATE (:Pokemon {
                name: $name, 
                type: $type, 
                evolution: $evolution, 
                total: $total, 
                hp: $hp, 
                attack: $attack
            })
        """
        parameters = {
            "name": name, 
            "type": type, 
            "evolution": evolution, 
            "total": total, 
            "hp": hp, 
            "attack": attack
        }
        self.db.execute_query(query,parameters)
        
        query2 = """
            MATCH (pokemon:Pokemon {name: $name})
            MERGE (typeNode:Type {name: $type})
            CREATE (pokemon)-[:IS_TYPE]->(typeNode)
        """
        parameters2 = {
            "name": name,
            "type": type
        }
        self.db.execute_query(query2,parameters2)
        print(colored(f'[-] Pokemon {name} criado com sucesso!', 'green'))

    def read_pokemon(self,name):
        query = """
            MATCH (p:Pokemon {name: $name}) 
            RETURN p.name AS name,
                   p.type AS type,
                   p.evolution AS evolution,
                   p.total AS total,
                   p.hp AS hp,
                   p.attack AS attack
        """
        
        parameters = {"name": name}
        result = self.db.execute_query(query, parameters)
        pokemon = result[0]
        if result:
            print(colored(f"[-] Nome: {pokemon['name']}", "light_green"))
            print(colored(f"[-] Tipo: {pokemon['type']}", "light_green"))
            print(colored(f"[-] Num. de Evolucao: {pokemon['evolution']}", "light_green"))
            print(colored(f"[-] Total: {pokemon['total']}", "light_green"))
            print(colored(f"[-] HP: {pokemon['hp']}", "light_green"))
            print(colored(f"[-] Ataque: {pokemon['attack']}", "light_green"))
        else:
            return colored('[-] Pokemon nao encontrado!', 'red')


    def update_pokemon(self,name,new_type,new_evolution,new_total,new_hp,new_attack):
        query = """
            MATCH(p:Pokemon {name: $name})
            SET p.type = $new_type,
                p.evolution = $new_evolution,
                p.total = $new_total,
                p.hp = $new_hp,
                p.attack = $new_attack 
        """
        parameters = {
            "name": name, 
            "new_type": new_type, 
            "new_evolution": new_evolution, 
            "new_total": new_total, 
            "new_hp": new_hp, 
            "new_attack": new_attack
        }
        self.db.execute_query(query,parameters)

    def delete_pokemon(self,name):
        query = "MATCH (p:Pokemon {name: $name}) DETACH DELETE p"
        parameters = {"name": name}
        self.db.execute_query(query,parameters)
        print(colored(f'[-] Pokemon {name} deletado com sucesso!', 'green'))

