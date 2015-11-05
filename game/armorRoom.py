import items, armor
from tiles import LootRoom

class FindApronRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Apron())

    def intro_text(self):
        return """
        You notice something shiny in the corner.
        It/'s an {}! You pick it up.
        """.format(self.name)
class FindStockPotRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.StockPot())

    def intro_text(self):
        return """
        You notice something shiny in the corner.
        It/'s a {}! You pick it up.
        """.format(self.name)
class FindOvenMittsRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.OvenMitts())

    def intro_text(self):
        return """
        You notice something shiny in the corner.
        It/'s {}! You pick it up.
        """.format(self.name)
class FindBakingSheetRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.BakingSheet())

    def intro_text(self):
        return """
        You notice something shiny in the corner.
        It/'s a {}! You pick it up.
        """.format(self.name)
class FindMixingBowlRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.MixingBowl())

    def intro_text(self):
        return """
        You notice something shiny in the corner.
        It/'s a {}! You pick it up.
        """.format(self.name)
class FindColanderRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Colander())

    def intro_text(self):
        return """
        You notice something shiny in the corner.
        It/'s a {}! You pick it up.
        """.format(self.name)
class FindDishTowelRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.DishTowel())

    def intro_text(self):
        return """
        You notice something shiny in the corner.
        It/'s a {}! You pick it up.
        """.format(self.name)
class FindTinFoilRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.TinFoil())

    def intro_text(self):
        return """
        You notice something shiny in the corner.
        It/'s {}! You pick it up.
        """.format(self.name)
