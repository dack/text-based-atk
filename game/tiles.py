import items, weapon, armor, enemies, world, actions

class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        """Information to be displayed when the player moves into this tile."""
        raise NotImplementedError()

    def modify_player(self, player):
        """Process actions that change the state of the player."""
        raise NotImplementedError()

    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves

    def available_actions(self):
        """Returns all of the available actions in this room."""
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())

        return moves

class StartingRoom(MapTile):
    def intro_text(self):
        return """
        You find yourself in a cave with a flickering torch on the wall.
        You can make out four paths, each equally as dark and foreboding.
        """

    def modify_player(self, player):
        #Room has no action on player
        pass


class EmptyCavePath(MapTile):
    def intro_text(self):
        return """
        Another unremarkable part of the cave. You must forge onwards.
        """

    def modify_player(self, player):
        #Room has no action on player
        pass

class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        MapTile.__init__(self, x, y)

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, player.hp))

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()

class CrinkleCookieRoom(EnemyRoom):
    def __init__(self, x, y):
        EnemyRoom.__init__(self, x, y, enemies.CrinkleCookie())

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
        EnemyRoom.__init__(self, x, y, enemies.BananaBread())

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
        EnemyRoom.__init__(self, x, y, enemies.Turkey())

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
        EnemyRoom.__init__(self, x, y, enemies.Yogurt())

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
        EnemyRoom.__init__(self, x, y, enemies.Jam())

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
        EnemyRoom.__init__(self, x, y, enemies.Cornbread())

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
        EnemyRoom.__init__(self, x, y, enemies.Coleslaw())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            Cackling Coleslaw Vermin have ambushed you!
            """
        else:
            return """
            The Coleslaw Vermin has been defeated.
            """

class CakePitRoom(MapTile):
    def intro_text(self):
        return """
        You have fallen into a pit of deadly cakes!
        You have died!
        """

    def modify_player(self, player):
        player.hp = 0

class LeaveCaveRoom(MapTile):
    def intro_text(self):
        return """
        You see a bright light in the distance...
        ... it grows as you get closer! It's sunlight!
        Victory is yours!
        """

    def modify_player(self, player):
        player.victory = True

#LootRoom
class LootRoom(MapTile):
    """A room that adds something to the player's inventory"""
    def __init__(self, x, y, item):
        self.item = item
        MapTile.__init__(self, x, y)

    def add_loot(self, player):
        player.inventory.append(self.item)

    def modify_player(self, player):
        self.add_loot(player)

#weapons
class FindCleaverRoom(LootRoom):
    def __init__(self, x, y):
        LootRoom.__init__(self, x, y, weapon.Cleaver())

    def intro_text(self):
        return """
        You notice something shiny in the corner.
        It\'s a {}! You pick it up.
        """.format(weapon.Cleaver().name)
class FindKnifeRoom(LootRoom):
    def __init__(self, x, y):
        LootRoom.__init__(self, x, y, weapon.Knife())

    def intro_text(self):
        return """
        You notice something shiny in the corner.
        It\'s a {}! You pick it up.
        """.format(weapon.Knife().name)
class FindSkilletRoom(LootRoom):
    def __init__(self, x, y):
        LootRoom.__init__(self, x, y, weapon.Skillet())

    def intro_text(self):
        return """
        You notice something shiny in the corner.
        It\'s a {}! You pick it up.
        """.format(weapon.Skillet().name)
class FindRollingPinRoom(LootRoom):
    def __init__(self, x, y):
        LootRoom.__init__(self, x, y, weapon.RollingPin())

    def intro_text(self):
        return """
        You notice something shiny in the corner.
        It\'s a {}! You pick it up.
        """.format(weapon.RollingPin().name)
class FindScissorsRoom(LootRoom):
    def __init__(self, x, y):
        LootRoom.__init__(self, x, y, weapon.Scissors())

    def intro_text(self):
        return """
        You notice something shiny in the corner.
        It\'s a {}! You pick it up.
        """.format(weapon.Scissors().name)
class FindLadleRoom(LootRoom):
    def __init__(self, x, y):
        LootRoom.__init__(self, x, y, weapon.Ladle())

    def intro_text(self):
        return """
        You notice something shiny in the corner.
        It\'s a {}! You pick it up.
        """.format(weapon.Ladle().name)
class FindSpatulaRoom(LootRoom):
    def __init__(self, x, y):
        LootRoom.__init__(self, x, y, weapon.Spatula())

    def intro_text(self):
        return """
        You notice something shiny in the corner.
        It\'s a {}! You pick it up.
        """.format(weapon.Spatula().name)
class FindTongsRoom(LootRoom):
    def __init__(self, x, y):
        LootRoom.__init__(self, x, y, weapon.Tongs())

    def intro_text(self):
        return """
        You notice something shiny in the corner.
        It\'s a {}! You pick it up.
        """.format(weapon.Tongs().name)
class FindPeelerRoom(LootRoom):
    def __init__(self, x, y):
        LootRoom.__init__(self, x, y, weapon.Peeler())

    def intro_text(self):
        return """
        You notice something shiny in the corner.
        It\'s a {}! You pick it up.
        """.format(weapon.Peeler().name)
#armor
class FindApronRoom(LootRoom):
    def __init__(self, x, y):
        LootRoom.__init__(self, x, y, armor.Apron())

    def intro_text(self):
        return """
        You notice something shiny in the corner.
        It\'s an {}! You pick it up.
        """.format(armor.Apron().name)
class FindStockPotRoom(LootRoom):
    def __init__(self, x, y):
        LootRoom.__init__(self, x, y, armor.StockPot())

    def intro_text(self):
        return """
        You notice something shiny in the corner.
        It\'s a {}! You pick it up.
        """.format(armor.StockPot().name)
class FindOvenMittsRoom(LootRoom):
    def __init__(self, x, y):
        LootRoom.__init__(self, x, y, armor.OvenMitts())

    def intro_text(self):
        return """
        You notice something shiny in the corner.
        It\'s {}! You pick it up.
        """.format(armor.OvenMitts().name)
class FindBakingSheetRoom(LootRoom):
    def __init__(self, x, y):
        LootRoom.__init__(self, x, y, armor.BakingSheet())

    def intro_text(self):
        return """
        You notice something shiny in the corner.
        It\'s a {}! You pick it up.
        """.format(armor.BakingSheet().name)
class FindMixingBowlRoom(LootRoom):
    def __init__(self, x, y):
        LootRoom.__init__(self, x, y, armor.MixingBowl())

    def intro_text(self):
        return """
        You notice something shiny in the corner.
        It\'s a {}! You pick it up.
        """.format(armor.MixingBowl().name)
class FindColanderRoom(LootRoom):
    def __init__(self, x, y):
        LootRoom.__init__(self, x, y, armor.Colander())

    def intro_text(self):
        return """
        You notice something shiny in the corner.
        It\'s a {}! You pick it up.
        """.format(armor.Colander().name)
class FindDishTowelRoom(LootRoom):
    def __init__(self, x, y):
        LootRoom.__init__(self, x, y, armor.DishTowel())

    def intro_text(self):
        return """
        You notice something shiny in the corner.
        It\'s a {}! You pick it up.
        """.format(armor.DishTowel().name)
class FindTinFoilRoom(LootRoom):
    def __init__(self, x, y):
        LootRoom.__init__(self, x, y, armor.TinFoil())

    def intro_text(self):
        return """
        You notice something shiny in the corner.
        It\'s {}! You pick it up.
        """.format(armor.TinFoil().name)
