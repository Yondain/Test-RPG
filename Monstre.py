import Joueur

import random

class Monster () :

    def __init__(self, stat):

        self.name = random.choice(["Slime", "Goblin", "Homme Lezard", "Ange Dechu", "Orias"])
        self.stat = stat

def randstat(lvljoueur):

        if (lvljoueur <= 15):
            stat = {"Atk": random.randrange(30, 1200, 50), "Pv": random.randrange(150, 2000, 50)}
        elif (15 <lvljoueur <= 99):
            stat = {"Atk": random.randrange(30, 50000, 50), "Pv": random.randrange(150, 300000, 50)}
        return stat

def creation(stati):
    m1= Monster(stati)
    return m1

"""
objectif: creer une classe pour chaque type de monstre

class Monster():
    def __init__(self):

        self.name=None
    def attack(self):
        return self.stat[Atk] """
    