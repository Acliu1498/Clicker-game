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
        # Print framerate and playtime in titlebar.
        text = "FPS: {0:.2f}   Playtime: {1:.2f}".format(self.clock.get_fps(), self.play_time)
        pygame.display.set_caption(text)
        # Update Pygame display.
        pygame.display.flip()

    def play_game(self):
        play = True

        while play:
            # current fps
            milliseconds = self.clock.tick(self.FPS)
            # gets user play time
            self.play_time += milliseconds / 1000.0
            # creates new enemy
            self.enemy = Enemy.Enemy(self.player.level)
            # checks if user wants to fight
            self.screen.fill((255, 255, 255))
            text_surface = self.font.render('Press space to fight!!', False, (0, 0, 0))
            self.screen.blit(text_surface, (200, 200))
            play = self.battle()
            self.print_frames()

    def battle(self):
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
                        if self.enemy.isDead():
                            return self.battle_end()
                    # User presses ESCAPE-Key
                    if event.key == pygame.K_ESCAPE:
                        return False

            self.print_frames()

    def battle_end(self):
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




if __name__ == '__main__':
    pygame.init()
    game = ClickerGame()
    game.play_game()
