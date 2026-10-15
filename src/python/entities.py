

class Entities():
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.max_health = health

    def take_damage(self, damage):
        self.health -= damage
        return self.is_alive()

    def heal_damage(self, heal):
        if self.health + heal > self.max_health:
            self.health = 100
        else:
            self.health += heal

    def is_alive(self):
        return self.health > 0