"""
Module Doc string
"""
from random import choice, randrange


def wear_and_tear():
    """
    returns random number between 0 & 2
    """
    return randrange(0, 2)


class Car:
    """
    Class description - car brands and any defects
    """
    def __init__(self, brand):
        self.brand = brand
        self.defect = None

    def take_damage(self):
        """
        Take Damage
        """
        if wear_and_tear():
            defects = ["brakes", "tires", "engine"]
            self.defect = choice(defects)
        else:
            self.defect = None
