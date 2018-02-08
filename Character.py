import random


class Character(object):

    def __init__(self):
        # character level
        self.__level = 0
        # character attack upper bound
        self.__atk_upper = 10
        # character attack lower bound
        self.__atk_lower = 5
        # character xp
        self.__xp = 0
        self.__xp2lvl = 100

    def attack(self):
        # returns a random attack between the bounds
        return random.randint(self.__atk_lower, self.__atk_upper)

    def lvl_up(self):
        # checks if enough to lvl up
        if self.__xp >= self.__xp2lvl:
            # increments level
            self.__level += 1
            # increases attack bounds
            self.__atk_upper += random.randint(5)
            self.__atk_lower += random.randint(5)
            # checks if the lower bound is greater then upper, if so swaps
            if self.__atk_lower > self.__atk_upper:
                t = self.__atk_upper
                self.__atk_upper = self.__atk_lower
                self.__atk_lower = t
            return True
        return False

    def add_xp(self, xp):
        self.__xp += xp

    def get_lvl(self):
        return self.__level
