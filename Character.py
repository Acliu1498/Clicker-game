import random


class Character(object):

    def __init__(self):
        # character level
        self.__level = 1
        # character attack upper bound
        self.__atk_upper = 15
        # character attack lower bound
        self.__atk_lower = 10
        # character xp
        self.__xp = 0
        self.__xp2lvl = 100

    def attack(self):
        # returns a random attack between the bounds
        return random.randint(self.__atk_lower, self.__atk_upper)

    def lvl_up(self):
        # checks if enough to lvl up
        if self.__xp >= self.__xp2lvl:
            self.__xp2lvl = int(self.__xp2lvl * 1.75)
            self.__xp = 0
            # increments level
            self.__level += 1
            # increases attack bounds
            self.__atk_upper += int(self.__atk_upper * 1/random.randrange(1, 10))
            self.__atk_lower += int(self.__atk_lower * 1/random.randrange(1, 10))
            # checks if the lower bound is greater then upper, if so swaps
            if self.__atk_lower > self.__atk_upper:
                t = self.__atk_upper
                self.__atk_upper = self.__atk_lower
                self.__atk_lower = t
            if self.__atk_upper - self.__atk_lower > (10 + (self.__level * 3)):
                self.__atk_lower = self.__atk_upper - (10 + (self.__level * 2))
            return True
        return False

    def get_atk_upper(self):
        return str(self.__atk_upper)

    def get_atk_lower(self):
        return str(self.__atk_lower)

    def get_lvl(self):
        return str(self.__level)

    def get_curr_xp(self):
        return str(self.__xp)

    def get_xp2lvl(self):
        return str(self.__xp2lvl)

    def add_xp(self, xp):
        self.__xp += xp

