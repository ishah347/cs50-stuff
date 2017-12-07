__author__ = 'Imran Shah'


"""Defines the enemies in the game"""

class Enemy:
    """A base class for all enemies"""
    def __init__(self, name, hp, damage):
        """Creates a new enemy

        :param name: the name of the enemy
        :param hp: the hit points of the enemy (if above 0, enemy is alive)
        :param damage: the damage the enemy does with each attack
        """
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0

"""Create enemies of various strengths and hp's to challenge player"""
class GiantSpider(Enemy):
    def __init__(self):
        super().__init__(name="Giant Spider", hp=10, damage=2)


class Ogre(Enemy):
    def __init__(self):
        super().__init__(name="Ogre", hp=30, damage=15)


class Cyclops(Enemy):
    def __init__(self):
        super().__init__(name="Cyclops", hp=50, damage=10)


class Dragon(Enemy):
    def __init__(self):
        super().__init__(name="Dragon", hp=100, damage=20)


class DavidMalan(Enemy):
    def __init__(self):
        super().__init__(name="David Malan", hp=1000, damage=1)
