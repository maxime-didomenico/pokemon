class Pokemon():

    def __init__(self, name, level, type, health, attack, defense, back_app, front_app):
        self.name = name
        self.level = level
        self.type = type
        self.health = health
        self.current_health = health
        self.attack = attack
        self.defense = defense
        self.back_app = back_app
        self.front_app = front_app