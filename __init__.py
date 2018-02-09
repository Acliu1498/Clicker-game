import pygame
import Character
import random
import Enemy
import image


class ClickerGame(object):

    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.back = None
        self.player = Character.Character()
        self.font = pygame.font.SysFont('Comic Sans MS', 48)
        self.enemy = None
        self.clock = pygame.time.Clock()
        self.FPS = 30
        self.play_time = 0.0

    def print_frames(self):
        """helper method to print the frames and update the display"""
        # Print framerate and playtime in titlebar.
        text = "FPS: {0:.2f}   Playtime: {1:.2f}".format(self.clock.get_fps(), self.play_time)
        pygame.display.set_caption(text)
        # Update Pygame display.
        pygame.display.flip()

    def play_game(self):
        """ main play function of the game"""
        play = True
        background = ['Images\\environment_forestbackground.png', 'Images\\environment_forestbackground1-1.png',
                      'Images\\environment_forest_evening.png']

        while play:
            # current fps
            milliseconds = self.clock.tick(self.FPS)
            # gets user play time
            self.play_time += milliseconds / 1000.0
            # creates new enemy
            self.enemy = Enemy.Enemy(self.player)
            # initializes background
            self.print_frames()
            self.screen.fill([255, 255, 255])
            self.back = image.Image(background[random.randint(0, 2)], [0, 0])
            self.screen.blit(self.back.image, self.back.rect)
            # asks user to fight
            text_surface = self.font.render('Press space to fight!!', False, (0, 0, 0))
            self.screen.blit(text_surface, (240, 300))
            # begins battle
            play = self.battle()

    def battle(self):
        """conducts battle for the game"""
        # while the game is on keep looping
        while True:
            for event in pygame.event.get():
                # User presses QUIT-button.
                if event.type == pygame.QUIT:
                    return False
                elif event.type == pygame.KEYDOWN:
                    # person presses space to attack
                    if event.key == pygame.K_SPACE:
                        # damages enemy
                        self.damage()
                        if self.enemy.is_dead():
                            return self.battle_end()
                    # User presses ESCAPE-Key
                    if event.key == pygame.K_ESCAPE:
                        return False
            self.draw_info()
            self.print_frames()

    def damage(self):
        """method damages enemy"""
        # gets player attack damage
        player_attack = self.player.attack()
        # does damage to enemy
        self.enemy.damage(player_attack)

        # location of the marker
        x = random.randint(300, 500)
        y = random.randint(250, 500)
        hit_marker = image.Image("Images\\Explosion (1).png", (x, y))
        hit_marker = pygame.transform.scale(hit_marker.image, (120, 120))
        self.screen.fill([255, 255, 255])
        # background
        self.screen.blit(self.back.image, self.back.rect)
        # enemy
        enemy_img = pygame.transform.scale(self.enemy.get_img().image, (350, 350))
        self.screen.blit(enemy_img, self.enemy.get_img().rect)
        # hit marker
        self.screen.blit(hit_marker, (x - 45, y - 25))
        # calculate damage
        text_surface = self.font.render("Attack Damage: " + str(player_attack), False, (0, 0, 0))
        self.screen.blit(text_surface, (230, 530))

    def battle_end(self):
        """at the end of the battle asks if the user wants to keep playing"""
        # once enemy is dead ask user if they want to play again
        self.screen.fill([255, 255, 255])
        self.screen.blit(self.back.image, self.back.rect)
        # if user leveled up levels up
        if self.check_lvl_up(self.enemy.get_xp()):
            text_surface = self.font.render('You Leveled Up!! Continue(Y/N)', False, (255, 255, 255))
        else:
            text_surface = self.font.render('You Defeated it!! Continue(Y/N)', False, (255, 255, 255))
        # writes text to surface
        self.screen.blit(text_surface, (50, 240))
        while True:
            for event in pygame.event.get():
                # exit if user tries to exit
                if event.type == pygame.QUIT:
                    return False
                elif event.type == pygame.KEYDOWN:
                    # person presses space to attack
                    if event.key == pygame.K_y:
                        return True
                    elif event.key == pygame.K_n or event.key == pygame.K_ESCAPE:
                        return False
            self.print_frames()

    def check_lvl_up(self, xp):
        """helper method to check if the user leveled up"""
        self.player.add_xp(xp)
        return self.player.lvl_up()

    def draw_info(self):
        """helper method to draw all the game info to screen"""
        info_font = pygame.font.SysFont('Comic Sans MS', 24)
        # draws enemy health
        pygame.draw.rect(self.screen, (0, 0, 0), (4, 9, 312, 42))
        pygame.draw.rect(self.screen, (0, 0, 0), (10, 15, 300, 30))
        pygame.draw.rect(self.screen, (255, 0, 0), (10, 15, 300 * (self.enemy.get_curr_health() /
                                                                   self.enemy.get_max_health()), 30))
        text_surface = info_font.render("Enemy Health: " + str(self.enemy.get_curr_health()), False, (255, 255, 255))
        self.screen.blit(text_surface, (10, 10))

        # draws player info
        pygame.draw.rect(self.screen, (0, 0, 0), (0, 87, 216, 201))
        pygame.draw.rect(self.screen, (255, 255, 255), (8, 95, 200, 185))
        text_surface = info_font.render("Player Info: ", False, (0, 0, 0))
        self.screen.blit(text_surface, (10, 100))
        # level
        text_surface = info_font.render("Level: " + self.player.get_lvl(), False, (0, 0, 0))
        self.screen.blit(text_surface, (10, 135))
        # attack
        text_surface = info_font.render("Attack: " + self.player.get_atk_lower() + " - " +
                                        self.player.get_atk_upper(), False, (0, 0, 0))
        self.screen.blit(text_surface, (10, 170))
        # xp
        text_surface = info_font.render("Xp: " + self.player.get_curr_xp(), False, (0, 0, 0))
        self.screen.blit(text_surface, (10, 205))
        # xp2nextlvl
        text_surface = info_font.render("Xp2NextLvl: " + self.player.get_xp2lvl(), False, (0, 0, 0))
        self.screen.blit(text_surface, (10, 240))


if __name__ == '__main__':
    pygame.init()
    game = ClickerGame()
    game.play_game()
