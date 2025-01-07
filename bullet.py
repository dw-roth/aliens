import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ A class to manage bullets fired from the game ship """

    def __init__(self, game, ship):
        """ Create a bullet object at the ships current position """
        pygame.sprite.Sprite.__init__(self)
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.bullet_color
        self.ship = ship

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ship.rect.midtop
        self.y = float(self.rect.y)
        
    def update(self):
        """ Move the bullet up the screen """
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw(self):
        """ Draw thyself on the screen """
        pygame.draw.rect(self.screen, self.color, self.rect)
