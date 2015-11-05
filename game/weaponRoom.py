import weapon
from tiles import LootRoom

class FindCleaverRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Cleaver())

    def intro_text(self):
        return """
        You notice something shiny in the corner.
        It/'s a {}! You pick it up.
        """.format(self.name)
class FindKnifeRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Knife())

    def intro_text(self):
        return """
        You notice something shiny in the corner.
        It/'s a {}! You pick it up.
        """.format(self.name)
class FindSkilletRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Skillet())

    def intro_text(self):
        return """
        You notice something shiny in the corner.
        It/'s a {}! You pick it up.
        """.format(self.name)
class FindRollingPinRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.RollingPin())

    def intro_text(self):
        return """
        You notice something shiny in the corner.
        It/'s a {}! You pick it up.
        """.format(self.name)
class FindScissorsRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Scissors())

    def intro_text(self):
        return """
        You notice something shiny in the corner.
        It/'s a {}! You pick it up.
        """.format(self.name)
class FindLadleRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Ladle())

    def intro_text(self):
        return """
        You notice something shiny in the corner.
        It/'s a {}! You pick it up.
        """.format(self.name)
class FindSpatulaRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Spatula())

    def intro_text(self):
        return """
        You notice something shiny in the corner.
        It/'s a {}! You pick it up.
        """.format(self.name)
class FindTongsRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Tongs())

    def intro_text(self):
        return """
        You notice something shiny in the corner.
        It/'s a {}! You pick it up.
        """.format(self.name)
class FindPeelerRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Peeler())

    def intro_text(self):
        return """
        You notice something shiny in the corner.
        It/'s a {}! You pick it up.
        """.format(self.name)
