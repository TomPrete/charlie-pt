from random import choice, randrange

class Car:

    def __init__(self, brand):
        self.brand = brand
        self.defect = None

    def wear_and_tear(self):
        return randrange(0,1)

    def take_damage(self):
        if self.wear_and_tear():
            defects = ['brakes', 'panel gaps', 'check engine', 'transmission']
            self.defect = choice(defects)
        else:
            self.defect = None

