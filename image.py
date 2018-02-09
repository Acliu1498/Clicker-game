import pygame


class Image(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        # initializes a new sprite
        pygame.sprite.Sprite.__init__(self)
        # gets image
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location