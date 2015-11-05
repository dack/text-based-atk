import random

class Enemy:
    def __init__(self, name, hp, damage, critChance):
        self.name = name
        self.gf = bool(random.getrandbits(1))
        self.sf = bool(random.getrandbits(1))
        self.hp = hp
        self.damage = damage + random.randint(1, 5) * critChance
        self.critChance = critChance

    def is_alive(self):
        return self.hp > 0
    def is_gf(self):
        if self.gf:
            return "Gluten Free"
        else:
            return null
    def is_sf(self):
        if self.sf:
            return "Sugar Free"
        else:
            return null

class CrinkleCookie(Enemy):
    def __init__(self):
        super().__init__(name="{} {} Crinkle Cookie Behemoth".format(self.is_gf, self.is_sf),
                         hp=5000,
                         damage=10,
                         critChance=.3)
class BananaBread(Enemy):
    def __init__(self):
        super().__init__(name="{} {} Banana Bread Berserker".format(self.is_gf, self.is_sf),
                         hp=1000,
                         damage=5,
                         critChance=.5)
class Turkey(Enemy):
    def __init__(self):
        super().__init__(name="{} {} Infernal Heritage Turkey".format(self.is_gf, self.is_sf),
                         hp=3000,
                         damage=4,
                         critChance=.2)
class Yogurt(Enemy):
    def __init__(self):
        super().__init__(name="{} {} Yogurt Brute".format(self.is_gf, self.is_sf),
                         hp=700,
                         damage=3,
                         critChance=.1)
class Jam(Enemy):
    jamFlavors = ["Rasberry", "Cherry", "Gooseberry", "Indiscriminate", "Strange", "Old", "Blueberry", "Rhubarb", "Orange", "Strawberry"]
    def __init__(self):
        super().__init__(name="{} {} {} Chu Jam".format(self.is_gf, self.is_sf, jamFlavors(random.randint(0, len(jamFlavors)-1))),
                         hp=500,
                         damage=3,
                         critChance=.1)
class Cornbread(Enemy):
    def __init__(self):
        super().__init__(name="{} {} Cornbread Fiend".format(self.is_gf, self.is_sf),
                         hp=300,
                         damage=5,
                         critChance=.1)
class Coleslaw(Enemy):
    def __init__(self):
        super().__init__(name="{} {} Coleslaw Vermin".format(self.is_gf, self.is_sf),
                         hp=100,
                         damage=1,
                         critChance=.05)
