import gold
from tiles import LootRoom

class Find5GoldRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Gold(5))

    def intro_text(self):
        return """
        Someone dropped a 5 gold piece. You pick it up.
        """

class Find10GoldRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Gold(10))

    def intro_text(self):
        return """
        Someone dropped a 10 gold piece. You pick it up.
        """

class Find50GoldRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Gold(50))

    def intro_text(self):
        return """
        Someone dropped a 50 gold piece. You pick it up.
        """
