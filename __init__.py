import pygame
import Character
import random
import Enemy


class ClickerGame(object):

    def __init__(self):
        self.screen = pygame.display.set_mode((600, 480))
        background = pygame.Surface(self.screen.get_size())
        background.fill((255, 255, 255))
        background = background.convert()
        self.screen.blit(background, (0, 0))
        self.player = Character.Character()
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
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

        while play:
            # current fps
            milliseconds = self.clock.tick(self.FPS)
            # gets user play time
            self.play_time += milliseconds / 1000.0
            # creates new enemy
            self.enemy = Enemy.Enemy(self.player.get_lvl())
            # checks if user wants to fight
            self.screen.fill((255, 255, 255))
            text_surface = self.font.render('Press space to fight!!', False, (0, 0, 0))
            self.screen.blit(text_surface, (150, 200))
            play = self.battle()
            self.print_frames()

    def battle(self):
        """conducts battle for the game"""
        # while the game is on keep looping
        while True:
            # creates enemy
            for event in pygame.event.get():
                # User presses QUIT-button.
                if event.type == pygame.QUIT:
                    return False
                elif event.type == pygame.KEYDOWN:
                    # person presses space to attack
                    if event.key == pygame.K_SPACE:
                        # gets player attack damage
                        player_attack = self.player.attack()
                        # does damage to enemy
                        self.enemy.damage(player_attack)
                        # calculate damage
                        text_surface = self.font.render(str(player_attack), False, (0, 0, 0))
                        # resets screen
                        self.screen.fill((255, 255, 255))
                        # writes damage to screen
                        self.screen.blit(text_surface, (random.randint(200, 400), random.randint(120, 300)))
                        if self.enemy.is_dead():
                            return self.battle_end()
                    # User presses ESCAPE-Key
                    if event.key == pygame.K_ESCAPE:
                        return False
            self.draw_info()
            self.print_frames()

    def battle_end(self):
        """at the end of the battle asks if the user wants to keep playing"""
        while True:
            # once enemy is dead ask user if they want to play again
            self.screen.fill((255, 255, 255))
            text_surface = self.font.render('You killed it!! Continue(Y/N)', False, (0, 0, 0))
            self.screen.blit(text_surface, (200, 200))
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

    def draw_info(self):
        pygame.draw.rect(self.screen, (0, 0, 0), (10, 20, 200, 10))
        pygame.draw.rect(self.screen, (255, 0, 0), (10, 20, 200 * (self.enemy.health / self.enemy.max_health), 10))

        info_font = pygame.font.SysFont('Comic Sans MS', 18)

        text_surface = info_font.render("Player Info: ", False, (0, 0, 0))
        self.screen.blit(text_surface, (10, 100))
        text_surface = info_font.render("Attack: ", False, (0, 0, 0))
        self.screen.blit(text_surface, (10, 120))
        text_surface = info_font.render("Xp: ", False, (0, 0, 0))
        self.screen.blit(text_surface, (10, 140))
        text_surface = info_font.render("Xp2NextLvl: ", False, (0, 0, 0))
        self.screen.blit(text_surface, (10, 160))




if __name__ == '__main__':
    pygame.init()
    game = ClickerGame()
    game.play_game()
