import items, random

class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage - (damage * durability)
        self.durability = random.randint(1, 5))/100
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)

class Cleaver(Weapon):
    def __init__(self):
        super().__init__(name="Meat Cleaver",
                         description="For cleaving meat.",
                         value=100,
                         damage=100
                         )
class Knife(Weapon):
    def __init__(self):
        super().__init__(name="Chef's Knife",
                         description="An 8 inch blade useful for mincing, slicing, and chopping.",
                         value=85,
                         damage=80
                         )
class Skillet(Weapon):
    def __init__(self):
        super().__init__(name="Cast Iron Skillet",
                         description="Don't forget to season with the blood of your enemies.",
                         value=75,
                         damage=70
                         )
class RollingPin(Weapon):
    def __init__(self):
        super().__init__(name="Rolling Pin",
                         description="It's a better weapon than a baguette.",
                         value=65,
                         damage=60
                         )
class Scissors(Weapon):
    def __init__(self):
        super().__init__(name="Scissors",
                         description="In case you needed a haircuit as well.",
                         value=55,
                         damage=50
                         )
class Ladle(Weapon):
    def __init__(self):
        super().__init__(name="Soup Ladle",
                         description="At least it's long?",
                         value=45,
                         damage=40
                         )
class Spatula(Weapon):
    def __init__(self):
        super().__init__(name="Spatula",
                         description="Good for slapping and grilled cheeses.",
                         value=45,
                         damage=40
                         )
class Tongs(Weapon):
    def __init__(self):
        super().__init__(name="Tongs",
                         description="Now you can pretend you're a crab! Pinch, pinch.",
                         value=35,
                         damage=30
                         )
class Peeler(Weapon):
    def __init__(self):
        super().__init__(name="Peeler",
                         description="Skin your carrots or your enemies!",
                         value=25,
                         damage=20
                         )
