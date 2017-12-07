__author__ = 'Imran Shah'
import random
import items, world

"""Establish the various states and actions available to the user"""
class Player():
    def __init__(self):
        self.inventory = [items.Gold(15), items.Rock()]
        self.hp = 100
        self.location_x, self.location_y = world.starting_position
        self.victory = False

    def is_alive(self):
        return self.hp > 0

    """Store the method used in the class Action in module "actions" so that the player can perform it"""
    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)

    """Have the player perform the action requested of him, with all things eventually neeeding to be returned in application.py being returned as self.act"""
    def print_inventory(self):
        self.act = self.inventory


    """Establish the equations used everytime a player tries to move"""
    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        self.act = ""

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)

    """Go through inventory and ensure that, when attacking, you use the best weapon in your inventory by comparing the damage values of the weapons"""
    def attack(self, enemy):
        best_weapon = None
        max_dmg = 0
        for i in self.inventory:
            if isinstance(i, items.Weapon):
                if i.damage > max_dmg:
                    max_dmg = i.damage
                    best_weapon = i

        enemy.hp -= best_weapon.damage
        if not enemy.is_alive():
            self.act = "You use %s against %s! You killed %s!" % (best_weapon.name, enemy.name, enemy.name)
        else:
            self.act = "You use %s against %s! %s HP is %s." % (best_weapon.name, enemy.name, enemy.name, enemy.hp)

    """If player tries to flee, his only options are to move to a random adjacent area to where he was before"""
    def flee(self, tile):
        """Moves the player randomly to an adjacent tile"""
        available_moves = tile.adjacent_moves()
        r = random.randint(0, len(available_moves) - 1)
        self.do_action(available_moves[r])
