import consumable
from tiles import LootRoom

class FindCookieRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Cookie())

    def intro_text(self):
        return """
        You notice something shiny in the corner.
        It/'s a {}! You pick it up.
        """.format(self.name)
class FindBreadRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Bread())

    def intro_text(self):
        return """
        You notice something shiny in the corner.
        It/'s {}! You pick it up.
        """.format(self.name)
class FindWMYogurtRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.WMYogurt())

    def intro_text(self):
        return """
        You notice something shiny in the corner.
        It/'s {}! You pick it up.
        """.format(self.name)
class FindFFYogurtRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.FFYogurt())

    def intro_text(self):
        return """
        You notice something shiny in the corner.
        It/'s {}! You pick it up.
        """.format(self.name)
class FindJellyRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Jelly())

    def intro_text(self):
        return """
        You notice something shiny in the corner.
        It/'s {}! You pick it up.
        """.format(self.name)
