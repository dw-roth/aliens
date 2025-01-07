""" Main module for Alien Invasion """
import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """ Main class to manage game assets and behavior. """

    def __init__(self):
        """ Initialize the game and create game resources """
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
             (self.settings.screen_width, self.settings.screen_height))
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption(self.settings.caption)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_alien_fleet()

    def run(self):
        """ Run the main loop for the game """
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)

    def _create_alien_fleet(self):
        """ Create the fleet of aliens """
        alien = Alien(self)
        x_pos = alien.rect.width

        while x_pos < (self.settings.screen_width - (2 * alien.rect.width)):
            self.aliens.add(self._create_alien(x_pos))
            x_pos += alien.rect.width * 2

    def _create_alien(self, x_pos):
        """ The work to create a new alien subsumed into this function """
        alien = Alien(self)
        alien.x = alien.rect.x = x_pos
        return alien
            
    def _check_events(self):
        """ Respond to keypresses and mouse events """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._handle_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._handle_keyup_event(event)
    
    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
                print(f"{len(self.bullets)} bullets active")

    def _handle_keydown_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.set_moving_right(True)
        elif event.key == pygame.K_LEFT:
            self.ship.set_moving_left(True)
        elif event.key == pygame.K_UP:
            self.ship.set_position_original()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()
            
    def _handle_keyup_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.set_moving_right(False)
        elif event.key == pygame.K_LEFT:
            self.ship.set_moving_left(False)
        
    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullet_limit:
            bullet = Bullet(self, self.ship)
            self.bullets.add(bullet)

    def _update_screen(self):
        """ Update images on the screen and flipt to the new screen """
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw()
        self.ship.blitme()
        self.aliens.draw(self.screen)

        # Make most recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
    # Create game instance and run game
    ai = AlienInvasion()
    ai.run()
