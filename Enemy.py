import Character
import image
import random


class Enemy(object):
    def __init__(self, player):
        images = ['Images\\horned-monster.png', 'Images\\frame-2.png',
                  'Images\\spiky-monster-game-obstacles-game-ornament.png', 'Images\\zombie.png']
        self.__max_health = 100 + (10 * random.randint(int(player.get_atk_lower()) - 1,
                                                        int(player.get_atk_upper()) + 1))
        self.__health = self.__max_health
        self.__xp = int((int(float(player.get_xp2lvl()))) * 1/(random.randint(int(player.get_lvl()),
                                                                              int(player.get_lvl()) + 3) + 2))
        self.__image = image.Image(images[random.randint(0, 3)], (250, 200))

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

    def get_img(self):
        return self.__image
