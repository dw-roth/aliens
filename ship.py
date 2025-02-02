import pygame

class Ship:
    """ A class to manage player's ship """

    def __init__(self, game):
        """ Initialize ship and set starting position """
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()


        # Load ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at bottom center of screen
        self.rect.midbottom = self.starting_position = self.screen_rect.midbottom
        self.moving_right = self.moving_left = False
    
        self.game = game
        
    def update(self):
        speed = self.game.settings.ship_speed
        if self.moving_right:
            if (self.rect.x + speed) <= (self.screen_rect.width - self.rect.width):
                self.rect.x += speed
        if self.moving_left:
            if (self.rect.x - speed) >= 0:
                self.rect.x -= speed

    def set_moving_right(self, val):
        self.moving_right = val

    def set_moving_left(self, val):
        self.moving_left = val

    def set_position_starting(self):
        self.rect.midbottom = self.starting_position

    def blitme(self):
        """ Draw the ship at its current location """
        self.screen.blit(self.image, self.rect)
