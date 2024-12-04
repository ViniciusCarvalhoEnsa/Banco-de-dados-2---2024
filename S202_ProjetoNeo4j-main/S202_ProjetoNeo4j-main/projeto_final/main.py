from database import Database
from cli import PokemonCLI
from pokemonMODEL import PokemonMODEL
from pokemon_database import PokemonDatabase
from termcolor import colored

db = Database("bolt://54.157.223.167:7687", "neo4j", "harmony-defeats-films")
#db.drop_all()

PokemonMODEL = PokemonMODEL(db)
pok = PokemonDatabase(db)

pokemonCLI = PokemonCLI(PokemonMODEL)
pokemonCLI.run()

def play_game():
    print(colored("[-] Bem vindo ao jogo!", "light_green"))
    print(colored("[-] As regras são simples. Voce tem que adivinhar alguns valores, caso acerte poderá abrir um pacote.\n", "light_green"))
    chute = int(input(colored("[!] Tente adivinhar quantos pokemons tem nesse database (caso voce criou algum pelo cli, conte o também):", "light_green")))
    res = pok.count_pokemon()
    if(chute==res):
        pok.open_packet()
    else:
        print(colored("[-] Chute incorreto =/","light_red"))
        print(colored("[-] Vamos tentar outra pergunta:","light_green"))
        print(colored("[-] Tente novamente.","light_green"))

    pokemonCLI.run()

aux = int(input("Quer jogar? Se sim 1, se nao 0:"))
if(aux==1):
    play_game()
else:
    pass

db.close()

