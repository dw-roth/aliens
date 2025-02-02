""" Main module for Alien Invasion """
import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button

class AlienInvasion:
    """ Main class to manage game assets and behavior. """

    def __init__(self):
        """ Initialize the game and create game resources """
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
             (self.settings.screen_width, self.settings.screen_height))
        
        # commented out code below is to set the game a full screen
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption(self.settings.caption)

        # Create an instance of GameStats to store game info
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_alien_fleet()
        self.game_active = False

        self.play_button = Button(self, "Start Game")

    def run(self):
        """ Run the main loop for the game """
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()
            self.clock.tick(60)

    def _create_alien_fleet(self):
        """ Create the fleet of aliens """
        alien = Alien(self)
        x_pos, y_pos = alien.rect.width, alien.rect.height

        while y_pos < (self.settings.screen_height - (7 * alien.rect.height)):
            while x_pos < (self.settings.screen_width - (2 * alien.rect.width)):
                self.aliens.add(self._create_alien(x_pos, y_pos))
                x_pos += alien.rect.width * 2
            
            x_pos = alien.rect.width
            y_pos += alien.rect.height * 2

    def _create_alien(self, x_pos, y_pos):
        """ The work to create a new alien subsumed into this function """
        alien = Alien(self)
        alien.x = alien.rect.x = x_pos
        alien.y = alien.rect.y = y_pos
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
    
    def _check_play_button(self, mouse_pos):
        """ Start a new game when the player clicks Start Game."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            self._start_game()

    def _start_game(self):
        self.stats.reset_stats()
        self.settings.initialize_dynamic_settings()
        self.bullets.empty()
        self.aliens.empty()
        self._create_alien_fleet()
        self.ship.set_position_starting()
        self.sb.prep_level()
        self.game_active = True
        pygame.mouse.set_visible(False)
        
    def _update_bullets(self):
        self.bullets.update()

        self._remove_out_of_range_bullets()
        self._remove_hit_aliens()
        if not self.aliens:
            self._reset_game()
            self.settings.increase_speed()
            self.stats.level += 1
            self.sb.prep_level()

    def _remove_out_of_range_bullets(self):
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _remove_hit_aliens(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points
            self.sb.prep_score()
            self.sb.check_high_score()

    def _update_aliens(self):
        self._check_alien_fleet_edges()
        self.aliens.update()

        #Look for ship-alien collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        self._check_aliens_bottom()

    def _ship_hit(self):
        """ Respond to the ship being hit by an alien """
        # Decrement remaining ships
        if self.stats.ships_remaining > 0:
            self.stats.ships_remaining -= 1
            self.sb.prep_ships()
            self._reset_game()

            # Pause
            sleep(0.5)
        else:
            self._reset_game()
            self._reset_level()
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _reset_game(self):
        self.bullets.empty()
        self.aliens.empty()
        self._create_alien_fleet()
        self.ship.set_position_starting()

    def _reset_level(self):
        self.sb.level = 1
        self.sb.prep_level()

    def _check_alien_fleet_edges(self):
        """ Move down and change directions if any single alien has reached an edge """
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _check_aliens_bottom(self):
        """ Check if any aliens have reached the bottom of the screen """
        for alien in self.aliens.sprites():
            if alien.rect.bottom > self.settings.screen_height:
                self._ship_hit()
                break;

    def _change_fleet_direction(self):
        """ drop the fleet and change direction """
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.alien_vert_speed

        self.settings.fleet_direction *= -1

    def _handle_keydown_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.set_moving_right(True)
        elif event.key == pygame.K_LEFT:
            self.ship.set_moving_left(True)
        elif event.key == pygame.K_UP:
            self.ship.set_position_starting()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p:
            self._start_game()
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

        # Draw the scoreboard
        self.sb.show_score()

        # Draw the start game button
        if not self.game_active:
            self.play_button.draw_button()

        # Make most recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
    # Create game instance and run game
    ai = AlienInvasion()
    ai.run()
