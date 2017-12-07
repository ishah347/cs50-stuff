__author__ = 'Imran Shah'


"""Describes the tiles in the world space."""

import items, enemies, actions, world

class MapTile:
    """The base class for a tile within the world space"""
    def __init__(self, x, y):
        """Creates a new tile.

        :param x: the x-coordinate of the tile
        :param y: the y-coordinate of the tile
        :param firstcalled: designates whether or not the variable is currently being used for the first time
        """
        self.x = x
        self.y = y
        self.firstcalled = True

    def getName(self):
        return self.__class__.__name__

    def intro_text(self):
        """Information necessary to be displayed when the player moves into this tile."""
        raise NotImplementedError()

    def modify_player(self, the_player):
        """Process actions that change the state of the player; is also necessary."""
        raise NotImplementedError()

    def adjacent_moves(self):
        """Returns all available move actions for adjacent tiles."""
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
        """The standardly used moves are the movement keys and looking at the player's inventory"""
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())

        return moves


class StartingRoom(MapTile):

    def intro_text(self):
        if self.firstcalled == True:
            self.firstcalled = False
            return """
            You find yourself in a cave with a flickering torch on the wall.
            You can make out four paths, each equally as dark and foreboding.
            """
        return """
        The room where your journey began. You must forge onwards.
        """

    def modify_player(self, the_player):
        #Room has no action on player
        return ""


class EmptyCavePath(MapTile):
    def intro_text(self):
        return """
        Another unremarkable part of the cave. You must forge onwards.
        """

    def modify_player(self, the_player):
        #Room has no action on player
        return ""


class SageRoom(MapTile):
    def intro_text(self):
        return """
        A wise sage tells you, "This is CS50."
        """

    def modify_player(self, the_player):
        #Room has no action on player
        return ""

"""Create class of rooms where items can be looted and added to the inventory."""
class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot(self, the_player):
        the_player.inventory.append(self.item)

    def modify_player(self, the_player):
        if self.firstcalled == False:
            self.firstcalled = None
            self.add_loot(the_player)
        return ""


class FindDaggerRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dagger())

    def intro_text(self):
        if self.firstcalled == True:
            self.firstcalled = False
            return """
            You notice something shiny in the corner.
            It's a dagger! You pick it up.
            """
        return """
        The room where you found the dagger. You must forge onwards.
        """


class FindSwordRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Sword())

    def intro_text(self):
        if self.firstcalled == True:
            self.firstcalled = False
            return """
            You see a sword in a stone.
            You pick it up with ease.
            """
        return """
        The room where you found the sword. You must forge onwards.
        """


class FindMasterSwordRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.MasterSword())

    def intro_text(self):
        if self.firstcalled == True:
            self.firstcalled = False
            return """
            Hey, the Master Sword? How'd that get here?!?!?
            You pick it up while trying not to fanboy out.
            """
        return """
        The room where you found the Master Sword. You must forge onwards.
        """


class Find5GoldRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Gold(5))

    def intro_text(self):
        if self.firstcalled == True:
            self.firstcalled = False
            return """
            Someone dropped a 5 gold piece. You pick it up.
            """
        return """
        The room where you found a 5 gold piece. You must forge onwards.
        """


class Find10GoldRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Gold(10))

    def intro_text(self):
        if self.firstcalled == True:
            self.firstcalled = False
            return """
            Someone dropped a 10 gold piece. You pick it up.
            """
        return """
        The room where you found a 10 gold piece. You must forge onwards.
        """


class Find50GoldRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Gold(50))

    def intro_text(self):
        if self.firstcalled == True:
            self.firstcalled = False
            return """
            Someone dropped a 50 gold piece. What luck! You pick it up.
            """
        return """
        The room where you found a 50 gold piece. You must forge onwards.
        """

"""Create a class of rooms where enemiies are located and battle requires that all actions other than attacking and fleeing, which had been unavailable, to be unavailable"""
class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            return "Enemy does %s damage. You have %s HP remaining.." % (self.enemy.damage, the_player.hp)
        else:
            return ""

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
            moves = self.adjacent_moves()
            moves.append(actions.ViewInventory())

            return moves


class GiantSpiderRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.GiantSpider())

    def intro_text(self):
        if self.enemy.is_alive():
            if self.firstcalled == True:
                self.firstcalled = False
                return """
                A giant spider jumps down from its web in front of you!
                """
            else:
                return ""
        else:
            if self.firstcalled == False:
                self.firstcalled = True
                return """
                The spider leaps at you.
                """
            else:
                return """
                The corpse of a dead spider rots on the ground.
                """


class OgreRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Ogre())

    def intro_text(self):
        if self.enemy.is_alive():
            if self.firstcalled == True:
                self.firstcalled = False
                return """
                An ogre is blocking your path!
                """
            else:
                return ""
        else:
            if self.firstcalled == False:
                self.firstcalled = True
                return """
                The ogre takes its last breath.
                """
            else:
                return """
                A dead ogre reminds you of your triumph.
                """


class CyclopsRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Cyclops())

    def intro_text(self):
        if self.enemy.is_alive():
            if self.firstcalled == True:
                self.firstcalled = False
                return """
                A cyclops ambushes you!
                """
            else:
                return ""
        else:
            if self.firstcalled == False:
                self.firstcalled = True
                return """
                The cyclops gives you a funny look.
                """
            else:
                return """
                A single bloody eye can be seen on the ground.
                """


class DragonRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Dragon())

    def intro_text(self):
        if self.enemy.is_alive():
            if self.firstcalled == True:
                self.firstcalled = False
                return """
                A dragon descends from the heavens!!!
                """
            else:
                return ""
        else:
            if self.firstcalled == False:
                self.firstcalled = True
                return """
                The dragon prepares to breathe fire.
                """
            else:
                return """
                The reptilian beast's carcass remains.
                """


class DavidMalanRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.DavidMalan())

    def intro_text(self):
        if self.enemy.is_alive():
            if self.firstcalled == True:
                self.firstcalled = False
                return """
                David Malan joins the battle!
                "This is CS50."
                """
            else:
                return ""
        else:
            if self.firstcalled == False:
                self.firstcalled = True
                return """
                "This is CS50."
                """
            else:
                return """
                "This was CS50."
                """

"""Create a room that heals you the first time you enter it, a room that instantly kills you when you enter it, and a room that, when entered, signifies victory"""
class HealingRoom(MapTile):
    def intro_text(self):
        if self.firstcalled == True:
            self.firstcalled = False
            return """
            You walk into an enchanted swamp and feel a strange sense of relaxation.
            """
        return """
        The swamp just stinks now. You must forge onwards.
        """

    def modify_player(self, player):
        if self.firstcalled == False:
            self.firstcalled = None
            player.hp += 20
            return "You've gained 20 hp!"
        return """"""


class SnakePitRoom(MapTile):
    def intro_text(self):
        return """
        You have fallen into a pit of deadly snakes!


        You have died...
        """

    def modify_player(self, player):
        player.hp = 0
        return "Restart to play again"

class LeaveCaveRoom(MapTile):
    def intro_text(self):
        return """
        You see a bright light in the distance...
        ... it grows as you get closer! It's sunlight!


        Victory is yours!
        """

    def modify_player(self, player):
        player.victory = True
        return "Restart to play again"