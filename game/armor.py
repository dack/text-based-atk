from items import Item
import random

class Armor(Item):
    def __init__(self, name, description, value, health):
        self.health = health
        Item.__init__(self, name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nHealth: {}".format(self.name, self.description, self.value, self.health)
    def getName():
        return self.name

class Apron(Armor):
    def __init__(self):
        Armor.__init__(self, name="Apron",
                         description="For keeping splatters off of your khakis.",
                         value=1000,
                         health=1000 + random.randint(50, 500))
class StockPot(Armor):
    def __init__(self):
        Armor.__init__(self, name="Stock Pot",
                         description="Can you even see?",
                         value=900,
                         health=900 + random.randint(50, 500))
class OvenMitts(Armor):
    def __init__(self):
        Armor.__init__(self, name="Oven Mitts",
                         description="Oven mitts or backup mittens?",
                         value=800,
                         health=800 + random.randint(50, 500))
class BakingSheet(Armor):
    def __init__(self):
        Armor.__init__(self, name="Baking Sheet",
                         description="Surprisingly bulletproof. To an extent.",
                         value=700,
                         health=700 + random.randint(50, 500))
class MixingBowl(Armor):
    def __init__(self):
        Armor.__init__(self, name="Mixing Bowl",
                         description="Looks like a helmet --from outer space.",
                         value=600,
                         health=600 + random.randint(50, 500))
class Colander(Armor):
    def __init__(self):
        Armor.__init__(self, name="Colander",
                         description="Made with breathable material.",
                         value=500,
                         health=500 + random.randint(50, 500))
class DishTowel(Armor):
    def __init__(self):
        Armor.__init__(self, name="Dish Towel",
                         description="Mutlipurpose cotton woven rectangle. Striped.",
                         value=400,
                         health=400 + random.randint(50, 500))
class TinFoil(Armor):
    def __init__(self):
        Armor.__init__(self, name="Tin Foil",
                         description="Actually aluminium, but does that really matter?",
                         value=200,
                         health=200 + random.randint(50, 500))
