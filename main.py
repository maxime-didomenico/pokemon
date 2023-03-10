from combat import Combat
from pokemon import Pokemon
import json
import random
import time

class Main():

    def __init__(self):
        pass


    def add_pokemon(self):
        name = input("Nom du Pokemon : ")
        level = 1
        type = input("Type du Pokemon : ")
        health = int(input("Vie du Pokemon : "))

        attack = int(input("Attaque du Pokemon : "))
        defense = int(input("Defense du Pokemon : "))

        with open('pokedex.json', 'r') as f:
            pokedex = json.load(f)

        pokedex.append({
            'nom': name,
            'level': level,
            'type': type,
            'health': health,
            'attack': attack,
            'defense': defense,
            'discovered': 'false'
        })

        with open('pokedex.json', 'w') as f:
            json.dump(pokedex, f, indent=4)


    def afficher_pokedex(self):
        with open('pokedex.json', 'r') as f:
            pokedex = json.load(f)

        i = 0
        for pokemon in pokedex:
            if pokemon['discovered'] == 'true':
                print(f"\nNom : {pokemon['nom']}\nLevel : {pokemon['level']}\nType : {pokemon['type']}\nVie : {pokemon['health']}\nAttaque : {pokemon['attack']}\nDefense : {pokemon['defense']}\n")
                i += 1
            else:
                pass
        
        if i == 0:
            print("\nYou haven't discovered any pokemon yet !\n")


    def menu(self):
        choice = 0
        while choice != 1 or choice != 2:
            print("\n1. I want to start a fight !\n2. I want to create or add a Pokemon\n3. Check my Pokedex\n4. Go home\n")
            choice = int(input("What would you like to do ?\n"))
            if choice >= 1 and choice <= 4:
                break

        if choice == 1:
            chosen_pokemon = []
            playable_pokemon = []

            print("\nWe attribute pokemon ...")

            with open('pokedex.json', 'r') as f:
                pokedex = json.load(f)

            # Create a list of available Pokemon (discovered != secret and not already chosen)
            playable_pokemon = [p for p in pokedex if p['discovered'] == 'true']

            if playable_pokemon == []:
                available_pokemon = [p for p in pokedex if p['discovered'] != 'secret' and p['nom'] not in chosen_pokemon]
                if len(available_pokemon) < 2:
                    print("Not enough Pokemon available.")
                    return 0

                # Print the list of available Pokemon and let the user choose one
                print("Choose a Pokemon:")
                for i, p in enumerate(available_pokemon):
                    print(f"{i+1}. {p['nom']}")

                pokemon1_index = int(input("Enter the number of the Pokemon you want to choose: ")) - 1
                pokemon1_data = available_pokemon[pokemon1_index]

                # Remove the chosen Pokemon from the list of available ones
                available_pokemon.remove(pokemon1_data)

                # Choose a random Pokemon from the list
                pokemon2_data = random.choice(available_pokemon)

                # Add the chosen Pokemon to the list of already chosen ones
                chosen_pokemon.extend([pokemon1_data['nom'], pokemon2_data['nom']])

                pokemon1 = Pokemon(pokemon1_data['nom'], pokemon1_data['level'], pokemon1_data['type'], pokemon1_data['health'], pokemon1_data['attack'], pokemon1_data['defense'], pokemon1_data['back_app'], pokemon1_data['front_app'])
                pokemon2 = Pokemon(pokemon2_data['nom'], pokemon2_data['level'], pokemon2_data['type'], pokemon2_data['health'], pokemon2_data['attack'], pokemon2_data['defense'], pokemon2_data['back_app'], pokemon2_data['front_app'])

                Combat(pokemon1, pokemon2).combat()
                return 0
            
            else:
                available_pokemon = [p for p in pokedex if p['discovered'] != 'secret' and p['nom'] not in chosen_pokemon]
                secret_pokemon = [p for p in pokedex if p['discovered'] == 'secret']

                if len(playable_pokemon) == 1:
                    pokemon1_data = playable_pokemon[0]
                    pokemon2_data = random.choice(available_pokemon)

                    # Add the chosen Pokemon to the list of already chosen ones
                    chosen_pokemon.extend([pokemon1_data['nom'], pokemon2_data['nom']])

                    pokemon1 = Pokemon(pokemon1_data['nom'], pokemon1_data['level'], pokemon1_data['type'], pokemon1_data['health'], pokemon1_data['attack'], pokemon1_data['defense'], pokemon1_data['back_app'], pokemon1_data['front_app'])
                    pokemon2 = Pokemon(pokemon2_data['nom'], pokemon2_data['level'], pokemon2_data['type'], pokemon2_data['health'], pokemon2_data['attack'], pokemon2_data['defense'], pokemon2_data['back_app'], pokemon2_data['front_app'])

                    Combat(pokemon1, pokemon2).combat()
                    return 0
            
                if len(playable_pokemon) > 1 and len(playable_pokemon) < 3:

                    # Print the list of available Pokemon and let the user choose one
                    print("Choose a Pokemon:")
                    for i, p in enumerate(playable_pokemon):
                        print(f"{i+1}. {p['nom']}")

                    pokemon1_index = int(input("Enter the number of the Pokemon you want to choose: ")) - 1
                    pokemon1_data = playable_pokemon[pokemon1_index]

                    # Choose a random Pokemon from the list
                    pokemon2_data = random.choice(playable_pokemon)

                    pokemon1 = Pokemon(pokemon1_data['nom'], pokemon1_data['level'], pokemon1_data['type'], pokemon1_data['health'], pokemon1_data['attack'], pokemon1_data['defense'], pokemon1_data['back_app'], pokemon1_data['front_app'])
                    pokemon2 = Pokemon(pokemon2_data['nom'], pokemon2_data['level'], pokemon2_data['type'], pokemon2_data['health'], pokemon2_data['attack'], pokemon2_data['defense'], pokemon2_data['back_app'], pokemon2_data['front_app'])

                    Combat(pokemon1, pokemon2).combat()
                    return 0
                
                if len(playable_pokemon) == 3:
                    print("But..")
                    time.sleep(2)
                    print("Wait...")
                    time.sleep(3)
                    print("Something is happenning...\n")
                    time.sleep(3)
                    print("A wild Mew appears !!!\n\nChoose a Pokemon ! :")
                    for i, p in enumerate(playable_pokemon):
                        print(f"{i+1}. {p['nom']}")

                    pokemon1_index = int(input("Enter the number of the Pokemon you want to choose: \n")) - 1
                    pokemon1_data = playable_pokemon[pokemon1_index]

                    # Choose a random Pokemon from the list
                    pokemon2_data = secret_pokemon[0]

                    # Add the chosen Pokemon to the list of already chosen ones
                    chosen_pokemon.extend([pokemon1_data['nom'], pokemon2_data['nom']])

                    pokemon1 = Pokemon(pokemon1_data['nom'], pokemon1_data['level'], pokemon1_data['type'], pokemon1_data['health'], pokemon1_data['attack'], pokemon1_data['defense'], pokemon1_data['back_app'], pokemon1_data['front_app'])
                    pokemon2 = Pokemon(pokemon2_data['nom'], pokemon2_data['level'], pokemon2_data['type'], pokemon2_data['health'], pokemon2_data['attack'], pokemon2_data['defense'], pokemon2_data['back_app'], pokemon2_data['front_app'])

                    Combat(pokemon1, pokemon2).combat()
                    return 0
                    

        elif choice == 2:
            self.add_pokemon()
            return 0

        elif choice == 3:
            self.afficher_pokedex()
            return 0

        elif choice == 4:
            exit()


    def main(self):
        print("\033[33m                                  ,\'\\")
        print("\033[33m    _.----.        ____         ,\'  _\\   ___    ___     ____")
        print("\033[33m_,-\'       `.     |    |  /`.   \\,-\'    |   \\  /   |   |    \\  |`.")
        print("\033[33m\\      __    \\    \'-.  | /   `.  ___    |    \\/    |   \'-.   \\ |  |")
        print("\033[33m \\.    \\ \\   |  __  |  |/    ,\',\'_  `.  |          | __  |    \\|  |")
        print("\033[33m   \\    \\/   /,\' _`.|      ,\' / / / /   |          ,\' _`.|     |  |")
        print("\033[33m    \\     ,-\'/  /   \\    ,\'   | \\/ / ,`.|         /  /   \\  |     |")
        print("\033[33m     \\    \\ |   \\_/  |   `-.  \\    `\'  /|  |    ||   \\_/  | |\\    |")
        print("\033[33m      \\    \\ \\      /       `-.`.____,-\'|  |\\  /| \\      /  | |   |")
        print("\033[33m       \\    \\ `.__,\'|  |`-._    `|      |__| \\/ |  `.__,\'|  | |   |")
        print("\033[33m        \\_.-\'       |__|    `-._ |              \'-.|     \'-.| |   |")
        print("\033[33m                                `\'                            \'-._|\033[0m")

        choice1 = 0

        while choice1 != 1 or choice1 != 2:
            choice1 = int(input("Do you want to :\n1. Start a new adventure ?\n2. Continue your last one ?\n"))
            
            if choice1 >= 1 and choice1 <= 2:
                break
        
        if choice1 == 1:
            with open('pokedex.json', 'r') as f:
                pokedex = json.load(f)
            
            for pokemon in pokedex:
                if pokemon['nom'] != 'Mew':
                    pokemon['discovered'] = 'false'

            with open('pokedex.json', 'w') as f:
                json.dump(pokedex, f, indent=4)

        if choice1 == 2:
            print("\nWelcome to your world of Pokemon !\n")

        while self.menu() == 0:
            self.menu()


main = Main()
main.main()