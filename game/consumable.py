import items, random

class Consumable(Item):
    def __init__(self, name, description, value, health):
        self.health = health
        super().__init__(name, description, value, health)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage, self.durability)

class Cookie(Consumable):
    def __init__(self):
        super().__init__(name="Cookie",
                         description="Restores 500 Health.",
                         value=200,
                         health=500)
class Bread(Consumable):
    def __init__(self):
        super().__init__(name="Bread",
                         description="Restores 400 Health.",
                         value=175,
                         health=400)
class WMYogurt(Consumable):
    def __init__(self):
        super().__init__(name="Whole Milk Yogurt",
                         description="Restores 300 Health.",
                         value=150,
                         health=300)
class FFYogurt(Consumable):
    def __init__(self):
        super().__init__(name="Fat Free Yogurt",
                         description="Restores 200 Health.",
                         value=100,
                         health=200)
class Jelly(Consumable):
    def __init__(self):
        super().__init__(name="Jelly",
                         description="Restores 50 Health.",
                         value=10,
                         health=50)
