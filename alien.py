import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ A class that respresents an alien """

    def __init__(self, game):
        """ Initialize the alien """
        pygame.sprite.Sprite.__init__(self)
        self.screen = game.screen

        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
