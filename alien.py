import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ A class that respresents an alien """

    def __init__(self, game):
        """ Initialize the alien """
        pygame.sprite.Sprite.__init__(self)
        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """ update the alien's position, left or right """
        self.x += self.settings.alien_horiz_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
