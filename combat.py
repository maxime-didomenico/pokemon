from pokemon import Pokemon
import random
import json

pow = [
        [["Normal"], ["Rock", "Steel"], 0.5],
        [["Normal"], ["Ghost"], 0],
        [["Fire"], ["Fire", "Water", "Rock", "Dragon"], 0.5],
        [["Fire"], ["Grass", "Ice", "Bug", "Steel"], 2],
        [["Water"], ["Water", "Grass", "Dragon"], 0.5],
        [["Water"], ["Fire", "Ground", "Rock"], 2],
        [["Electric"], ["Electric", "Grass", "Dragon"], 0.5],
        [["Electric"], ["Water", "Flying"], 2],
        [["Grass"], ["Fire", "Grass", "Poison", "Flying", "Bug", "Dragon", "Steel"], 0.5],
        [["Grass"], ["Water", "Ground", "Rock"], 2],
        [["Ice"], ["Fire", "Water", "Ice", "Steel"], 0.5],
        [["Ice"], ["Grass", "Ground", "Flying", "Dragon"], 2],
        [["Fighting"], ["Poison", "Flying", "Psychic", "Bug", "Fairy"], 0.5],
        [["Fighting"], ["Normal", "Ice", "Rock", "Dark", "Steel"], 2],
        [["Poison"], ["Poison", "Ground", "Rock", "Ghost"], 0.5],
        [["Poison"], ["Grass", "Fairy"], 2],
        [["Ground"], ["Grass", "Bug"], 0.5],
        [["Ground"], ["Fire", "Electric", "Poison", "Rock", "Steel"], 2],
        [["Flying"], ["Electric", "Rock", "Steel"], 0.5],
        [["Flying"], ["Grass", "Fighting", "Bug"], 2],
        [["Psychic"], ["Psychic", "Steel"], 0.5],
        [["Psychic"], ["Fighting", "Poison"], 2],
        [["Bug"], ["Fire", "Fighting", "Poison", "Flying", "Ghost", "Steel", "Fairy"], 0.5],
        [["Bug"], ["Grass", "Psychic", "Dark"], 2],
        [["Rock"], ["Fighting", "Ground", "Steel"], 0.5],
        [["Rock"], ["Fire", "Ice", "Flying", "Bug"], 2],
        #[["Ghost"], ["Normal", "Psychic"], 0],
        #[["Ghost"], ["Ghost", "Dark"], 2],
        [["Dragon"], ["Steel"], 0.5],
        [["Dragon"], ["Dragon"], 2],
        #[["Dark"], ["Fighting", "Dark", "Fairy"], 0.5],
        #[["Dark"], ["Psychic", "Ghost"], 2],
        [["Steel"], ["Fire", "Water", "Electric", "Steel"], 0.5],
        [["Steel"], ["Ice", "Rock", "Fairy"], 2],
        [["Fairy"], ["Fire", "Poison", "Steel"], 0.5],
        [["Fairy"], ["Fighting", "Dragon", "Dark"], 2]
    ]

class Combat():

    def __init__(self, pokemon1, pokemon2):

        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2


    def special_attack(self, pokemon1, pokemon2):
        miss = random.randint(1, 4)
        p1_type = pokemon1.type.lower().capitalize()
        p2_type = pokemon2.type.lower().capitalize()
        p1_effective = 1
        p2_effective = 1

        for p in pow:
            if p[0][0] == p1_type and p2_type in p[1]:
                p1_effective *= p[2]
            if p[0][0] == p2_type and p1_type in p[1]:
                p2_effective *= p[2]
        effective = p1_effective / p2_effective

        if miss == 1:
            att = 0

        else:
            att = int(((((pokemon1.level * 0.4 + 2) * pokemon1.attack * effective) / (pokemon2.defense / 50)) + 2) / 10)
            pokemon2.current_health -= att

        return att


    def attack(self, pokemon1, pokemon2):
        
        miss = random.randint(1, 4)
        if miss == 1:
                att = 0
        else:
            pow = 1
            att = int(((((pokemon1.level * 0.4 + 2) * pokemon1.attack * pow) / (pokemon2.defense / 50)) + 2) / 10)
            pokemon2.current_health -= att
        return(att)


    def print_stats(self):

        print("\n +------------------------------------+\n", "  ",self.pokemon1.id, "has", '\033[32m', self.pokemon1.current_health, '\033[0m', "health left     ")
        print("   ", self.pokemon2.id, "has", "\033[31m", self.pokemon2.current_health, '\033[0m', "health left     \n", "+------------------------------------+\n")


    def check_loose(self):

        if self.pokemon1.current_health <= 0 and self.pokemon2.current_health <= 0:
            self.pokemon1.current_health = 0
            self.pokemon2.current_health = 0
            print("It's a draw !")

        if self.pokemon1.current_health <= 0:

            self.pokemon1.current_health = 0
            self.print_stats()
            print(self.pokemon2.id, "has won the battle!\nYou Loose !")
        
        if self.pokemon2.current_health <= 0:

            self.pokemon2.current_health = 0
            self.print_stats()
            print(self.pokemon1.id, "has won the battle!\nYou Win !")

            with open('pokedex.json') as f:
                pokedex = json.load(f)

            for pokemon in pokedex:
                if pokemon['nom'] == self.pokemon2.id:
                    if pokemon['discovered'] == 'true':
                        print(f'{self.pokemon2.id} is already discovered !')
                    
                    else:
                        pokemon['discovered'] = 'true'
                        print(f'{self.pokemon2.id} has been discovered !')
                
                    with open('pokedex.json', 'w') as f:
                        json.dump(pokedex, f, indent=4)
                
            return 1


    def combat(self):
        
        print('\n')
        while self.pokemon1.current_health > 0 and self.pokemon2.current_health > 0:
            choice = 0

            while choice != 1 or choice != 2:

                list_pokemon = ["Bulbizarre", "Salameche", "Carapuce","Mew"]
                color_list = ["\033[32m", "\033[31m", "\u001b[36m", "\u001b[35m"]
                for pokemon in list_pokemon:
                    if pokemon == self.pokemon2.id:
                        print(color_list[list_pokemon.index(pokemon)], self.pokemon2.front_app, '\033[0m')

                for pokemon in list_pokemon:
                    if pokemon == self.pokemon1.id:
                        print(color_list[list_pokemon.index(pokemon)], self.pokemon1.back_app, '\033[0m')

                self.print_stats()

                choice = int(input("What will you do ?\n1. Attack\n2. Special Attack\n"))
                print(' ')

                if choice == 1 or choice == 2:
                    break
                else:
                    print("Invalid input, please try again\n")
            
            if choice == 1:
                att = self.attack(self.pokemon1, self.pokemon2)
                if att == 0:
                    print(f"{self.pokemon1.id} missed !")
                else :
                    print(f"{self.pokemon1.id} used attack and inflicted", '\033[32m', att, '\033[0m', "damage")

            elif choice == 2:
                att = self.special_attack(self.pokemon1, self.pokemon2)
                if att == 0:
                    print(f"{self.pokemon1.id} missed !")
                else :
                    print(f"{self.pokemon1.id} used attack and inflicted", '\033[32m', att, '\033[0m', "damage")

            if self.check_loose() != 1:
                opponent_choice = random.randint(1, 2)

                if opponent_choice == 1:
                    att = self.attack(self.pokemon2, self.pokemon1)
                    if att == 0:
                        print(f"{self.pokemon2.id} missed !")
                    else :
                        print(f"{self.pokemon2.id} used attack and inflicted", '\033[31m', att, '\033[0m', "damage")

                elif opponent_choice == 2:
                    att = self.special_attack(self.pokemon2, self.pokemon1)
                    if att == 0:
                        print(f"{self.pokemon2.id} missed !")
                    else :
                        print(f"{self.pokemon2.id} used special attack and inflicted", '\033[31m', att, '\033[0m', "damage")

                self.check_loose()