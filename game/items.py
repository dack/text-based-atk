import random

class Item():
        #base item class
        def __init__(self, name, description, value):
            self.name = name
            self.description = description
            self.value = value

        def __str__(self):
            return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

#weapons
class Weapon(Item):
    def __init__(self, name, description, value, damage):
        durability = random.randint(1, 5)/100
        self.damage = damage - (damage * durability)
        Item.__init__(self, name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)

class Cleaver(Weapon):
    def __init__(self):
        Weapon.__init__(self, name="Meat Cleaver",
                         description="For cleaving meat.",
                         value=100,
                         damage=100
                         )
class Knife(Weapon):
    def __init__(self):
        Weapon.__init__(self, name="Chef's Knife",
                         description="An 8 inch blade useful for mincing, slicing, and chopping.",
                         value=85,
                         damage=80
                         )
class Skillet(Weapon):
    def __init__(self):
        Weapon.__init__(self, name="Cast Iron Skillet",
                         description="Don't forget to season with the blood of your enemies.",
                         value=75,
                         damage=70
                         )
class RollingPin(Weapon):
    def __init__(self):
        Weapon.__init__(self, name="Rolling Pin",
                         description="It's a better weapon than a baguette.",
                         value=65,
                         damage=60
                         )
class Scissors(Weapon):
    def __init__(self):
        Weapon.__init__(self, name="Scissors",
                         description="In case you needed a haircuit as well.",
                         value=55,
                         damage=50
                         )
class Ladle(Weapon):
    def __init__(self):
        Weapon.__init__(self, name="Soup Ladle",
                         description="At least it's long?",
                         value=45,
                         damage=40
                         )
class Spatula(Weapon):
    def __init__(self):
        Weapon.__init__(self, name="Spatula",
                         description="Good for slapping and grilled cheeses.",
                         value=45,
                         damage=40
                         )
class Tongs(Weapon):
    def __init__(self):
        Weapon.__init__(self, name="Tongs",
                         description="Now you can pretend you're a crab! Pinch, pinch.",
                         value=35,
                         damage=30
                         )
class Peeler(Weapon):
    def __init__(self):
        Weapon.__init__(self, name="Peeler",
                         description="Skin your carrots or your enemies!",
                         value=25,
                         damage=20
                         )
#armor
class Armor(Item):
    def __init__(self, name, description, value, health):
        self.health = health
        Item.__init__(self, name, description, value, health)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nHealth: {}".format(self.name, self.description, self.value, self.health)

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
