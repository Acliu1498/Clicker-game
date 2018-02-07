import random


class Character(object):

    def __init__(self):
        # character level
        self.level = 0
        # character attack upper bound
        self.atk_upper = 10
        # character attack lower bound
        self.atk_lower = 5

    def attack(self):
        # returns a random attack between the bounds
        return random.randint(self.atk_lower, self.atk_upper)

