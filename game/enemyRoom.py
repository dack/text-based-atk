import enemies
from tiles import EnemyRoom

class CrinkleCookieRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.CrinkleCookie())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            You hear a loud thump and a Crinkle Cookie Behemoth lands in front of you!
            """
        else:
            return """
             A dead Crinkle Cookie reminds you of your triumph.
            """
class BananaBreadRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.BananaBread(())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A crazed Banana Bread lunges at you!
            """
        else:
            return """
            The corpse of a dead Banana Bread rots on the ground.
            """
class TurkeyRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Turkey())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A basted beast appears!
            """
        else:
            return """
            The Infernal Heritage Turkey is roasted.
            """
class YogurtRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Yogurt())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A Yogurt Brute has become enraged!
            """
        else:
            return """
            The probitoic remnants form a puddle at your feet.
            """
class JamRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Jam())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            PUMP UP THE JAAAAAAAAM
            """
        else:
            return """
            The Jam is dead.
            """
class CornbreadRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Cornbread())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A corny fiend has been trailing you!
            """
        else:
            return """
            The Cornbread has been slain.
            """
class ColeslawRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Coleslaw())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            Cackling Coleslaw Vermin have ambushed you!
            """
        else:
            return """
            The Coleslaw Vermin has been defeated.
            """
