import Character


class Enemy(object):
    def __init__(self, player):
        self.__max_health = 100 + (100 * int(player.get_lvl()))
        self.__health = self.__max_health
        self.__xp = int((int(float(player.get_xp2lvl()))) * 1/(int(player.get_lvl()) + 2))

    def damage(self, dmg):
        self.__health -= dmg

    def get_curr_health(self):
        return self.__health

    def get_max_health(self):
        return self.__max_health

    def is_dead(self):
        return self.__health <= 0

    def get_xp(self):
        return self.__xp
