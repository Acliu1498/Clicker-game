import pygame
import Character
import random


class ClickerGame(object):

    def __init__(self):
        self.screen = pygame.display.set_mode((600, 480))
        background = pygame.Surface(self.screen.get_size())
        background.fill((255, 255, 255))
        background = background.convert()
        self.screen.blit(background, (0, 0))
        self.player = Character.Character()

    def play_game(self):
        # game clock
        clock = pygame.time.Clock()
        # fps of game
        FPS = 30
        # the play time
        playtime = 0.0
        # generates font
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        # bool to play game
        game_on = True
        # while the game is on keep looping
        while game_on:
            milliseconds = clock.tick(FPS)
            playtime += milliseconds / 1000.0

            for event in pygame.event.get():
                # User presses QUIT-button.
                if event.type == pygame.QUIT:
                    game_on = False
                elif event.type == pygame.KEYDOWN:
                    # person presses space to attack
                    if event.key == pygame.K_SPACE:
                        # gets player attack damage
                        player_attack = self.player.attack()
                        textsurface = myfont.render(str(player_attack), False, (0, 0, 0))
                        self.screen.fill((255, 255, 255))
                        self.screen.blit(textsurface, (random.randint(200, 400), random.randint(120, 300)))
                    # User presses ESCAPE-Key
                    if event.key == pygame.K_ESCAPE:
                        game_on = False

            # Print framerate and playtime in titlebar.
            text = "FPS: {0:.2f}   Playtime: {1:.2f}".format(clock.get_fps(), playtime)
            pygame.display.set_caption(text)

            # Update Pygame display.
            pygame.display.flip()

if __name__ == '__main__':
    game = ClickerGame()
    game.play_game()
