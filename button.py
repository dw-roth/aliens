import pygame.font

class Button:
    def __init__(self, game, msg):
        """ Initialize button attributes """
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        # Set dimensions and properties of button
        self.width, self.height = 200, 50
        self.background_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """ Turn msg into rendered image and center text """
        self.msg_image = self.font.render(msg, True, self.text_color, self.background_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """ Draw blank button and then draw image """
        self.screen.fill(self.background_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

