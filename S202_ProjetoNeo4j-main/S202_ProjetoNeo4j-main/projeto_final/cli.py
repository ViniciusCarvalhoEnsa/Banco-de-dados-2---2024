from termcolor import colored

class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input(colored("[+] Insira um comando: ", "light_yellow"))
            if command == "quit":
                print(colored("[-] Fechando...", "light_red"))
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print(colored("[!] Comando invalido. Tente de novo.", "red"))

class PokemonCLI(SimpleCLI):
    def __init__(self, pokemon_db):
        super().__init__()
        self.pokemon_db = pokemon_db
        self.add_command("create", self.create_pokemon)
        self.add_command("read", self.read_pokemon)
        self.add_command("update", self.update_pokemon)
        self.add_command("delete", self.delete_pokemon)
    
    def create_pokemon(self):
        name = input(colored("[+] Entre com o nome do Pokemon, de preferencia em ingles: ","light_yellow"))
        type = input(colored("[+] Entre com o tipo do Pokemon, de preferencia em ingles: ", "light_yellow"))
        evolution = int(input(colored("[+] Entre com numero da evolucao do Pokemon(exemplo 1 = basico): ", "light_yellow")))
        total = int(input(colored("[+] Entre com numero total do Pokemon: ","light_yellow")))
        hp = int(input(colored("[+] Entre com os Pontos de Saude do Pokemon: ","light_yellow")))
        attack = int(input(colored("[+] Entre com o valor do ataque do Pokemon: ", "light_yellow")))
        self.pokemon_db.create_pokemon(name,type,evolution,total,hp,attack)

    def read_pokemon(self):
        name = input(colored("[+] Entre com o nome do Pokemon, de preferencia em ingles, do Pokemon que deseja encontrar: ", "light_yellow"))
        self.pokemon_db.read_pokemon(name)
        
    def update_pokemon(self):
        name = input(colored("[+] Entre com o nome do Pokemon, de preferencia em ingles, do Pokemon que deseja alterar: ", "light_yellow"))
        type = input(colored("[+] Entre com o novo tipo do Pokemon, de preferencia em ingles: ", "light_yellow"))
        evolution = int(input(colored("[+] Entre com o novo numero da evolucao do Pokemon(exemplo 1 = basico): ", "light_yellow")))
        total = int(input(colored("[+] Entre com o novo numero total do Pokemon: ", "light_yellow")))
        hp = int(input(colored("[+] Entre com os novos Pontos de Saude do Pokemon: ", "light_yellow")))
        attack = int(input(colored("[+] Entre com o novo valor do ataque do Pokemon: ", "light_yellow")))
        self.pokemon_db.update_pokemon(name,type,evolution,total,hp,attack)

    def delete_pokemon(self):
        name = input(colored("[+] Entre com o nome do Pokemon, de preferencia em ingles, do Pokemon que deseja deletar: ", "light_yellow"))
        self.pokemon_db.delete_pokemon(name)

    def run(self):
        print("                                  ,'\\")
        print("    _.----.        ____         ,'  _\\   ___    ___     ____")
        print(" _,-'       `.     |    |  /`.   \\,-'    |   \\  /   |   |    \\  |`.")
        print(" \\      __    \\    '-.  | /   `.  ___    |    \\/    |   '-.   \\ |  |")
        print("  \\.    \\ \\   |  __  |  |/    ,','_  `.  |          | __  |    \\|  |")
        print("    \\    \\/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |")
        print("     \\     ,-'/  /   \\    ,'   | \\/ / ,`.|         /  /   \\  |     |")
        print("      \\    \\ |   \\_/  |   `-.  \\    `'  /|  |    ||   \\_/  | |\\    |")
        print("       \\    \\ \\      /       `-.`.___,-' |  |\\  /| \\      /  | |   |")
        print("        \\    \\ `.__,'|  |`-._    `|      |__| \\/ |  `.__,'|  | |   |")
        print("         \\_.-'       |__|    `-._ |              '-.|     '-.| |   |")
        print("                                `'                            '-._|")
        print(colored("[-] Bem-Vindo ao POKEMON CLI!", "green"))
        print(colored("[-] Comandos disponiveis: create, read, update, delete, quit", "green"))
        super().run()

