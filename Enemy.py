
class Enemy(object):
    def __init__(self, player_lvl):
        self.max_health = 100 + (100 * player_lvl)
        self.health = self.max_health

    def damage(self, dmg):
        self.health -= dmg

    def is_dead(self):
        return self.health <= 0
