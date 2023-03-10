class Pokemon():

    def __init__(self, name, level, type, health, attack, defense, back_app, front_app):
        self.__name = name
        self.level = level
        self.type = type
        self.__health = health
        self.current_health = health
        self.attack = attack
        self.defense = defense
        self.back_app = back_app
        self.front_app = front_app

    def get_name(self):
        return self.__name
    
    def get_health(self):
        return self.__health
    
    def set_health(self, health):
        self.__health = health