import random

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
            self.health = self.max_health
        else:
            self.health += heal

    def is_alive(self):
        return self.health > 0
    
    
    def __str__(self):
        return f"{self.name} - Health: {self.health}, Attack: {self.attack}, Defense: {self.defense}"
    
    
    
class Enemies(Entities):
    def __init__(self, name, health, attack, defense):
        super().__init__(name, health, attack, defense)
        self.loot = []
        self.exp = 0
        self.gold = 0