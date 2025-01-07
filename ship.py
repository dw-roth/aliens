import pygame

class Ship:
    """ A class to manage player's ship """

    def __init__(self, game):
        """ Initialize ship and set starting position """
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        print("Initializing ship")
        print(f"screen rect: {self.screen_rect}")


        # Load ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        print(f"ship rect: {self.rect}")

        # Start each new ship at bottom center of screen
        self.rect.midbottom = self.original_position = self.screen_rect.midbottom
        self.moving_right = self.moving_left = False
        print(f"screen midbottom: {self.screen_rect.midbottom}")
        print(f"ship midbottom: {self.rect.midbottom}")
    
        self.game = game
        self.speed = 2
        
    def update(self):
        if self.moving_right:
            if (self.rect.x + self.speed) <= (self.screen_rect.width - self.rect.width):
                self.rect.x += self.speed
        if self.moving_left:
            if (self.rect.x - self.speed) >= 0:
                self.rect.x -= self.speed

    def set_moving_right(self, val):
        self.moving_right = val

    def set_moving_left(self, val):
        self.moving_left = val

    def set_position_original(self):
        self.rect.midbottom = self.original_position

    def blitme(self):
        """ Draw the ship at its current location """
        self.screen.blit(self.image, self.rect)
