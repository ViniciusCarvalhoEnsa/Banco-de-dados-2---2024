from database import Database
from cli import PokemonCLI
from pokemonMODEL import PokemonMODEL

db = Database("bolt://54.157.223.167:7687", "neo4j", "harmony-defeats-films")
#db.drop_all()

PokemonMODEL = PokemonMODEL(db)

pokemonCLI = PokemonCLI(PokemonMODEL)
pokemonCLI.run()

db.close()

