__author__ = 'Imran Shah'


"""Describes the items in the game."""

class Item():
    """The base class for all items

        :param name: the name of the item
        :param description: a description of the item
        :param value: how much item is worth
        """
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    """Create format for how each item in the inventory will be described when listened."""
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

"""Create class of weapons among items and several examples of weapons of various strengths to be found in the game. The element of
damage for an item to perform is also introduced."""
class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)


class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
                         description="A fist-sized rock, suitable for bludgeoning.",
                         value=0,
                         damage=5)


class Dagger(Weapon):
    def __init__(self):
        super().__init__(name="Dagger",
                         description="A small dagger with some rust. Somewhat more dangerous than a rock.",
                         value=10,
                         damage=20)


class Sword(Weapon):
    def __init__(self):
        super().__init__(name="Sword",
                         description="Forged by a local blacksmith. Is of great power.",
                         value=20,
                         damage=50)


class MasterSword(Weapon):
    def __init__(self):
        super().__init__(name="Master Sword",
                         description="The one from Legend of Zelda. Yup",
                         value=100,
                         damage=999)

"""Create gold for player to collect"""
class Gold(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Gold",
                         description="A round coin with {} stamped on the front.".format(str(self.amt)),
                         value=self.amt)
