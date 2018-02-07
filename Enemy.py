
class Enemy(object):
    def __init__(self, player_lvl):
        self.health = 100 + (100 * player_lvl)

    def damage(self, dmg):
        self.health -= dmg

    def isDead(self):
        return self.health <= 0
