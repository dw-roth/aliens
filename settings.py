class Settings:
    """ Module to manage game settings """

    def __init__(self):
        """ Initialize game settings """
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.caption = "Alien Invasion"

        # ship settings
        self.ship_limit = 3

        # bullet settings
        self.bullet_speed = 4
        self.bullet_width = 8
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

        # alien settings
        self.alien_horiz_speed = 1
        self.alien_vert_speed = 10

        self.bullet_speedup_scale = 1.6 
        self.alien_horiz_speedup_scale = 1.3 
        self.alien_vert_speedup_scale = 10
        self.ship_speedup_scale = 1.5
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ initialize the dynamic settings """

        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_horiz_speed = 1.0
        self.alien_vert_speed = 1.0
        self.bullet_limit = 8

        # 1 = moving horizontal to right
        # -1 = moving horizontal to left
        self.fleet_direction = 1

        # Score settings
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.ship_speedup_scale
        if self.bullet_speed < 16:
            self.bullet_speed *= self.bullet_speedup_scale
        self.alien_horiz_speed *= self.alien_horiz_speedup_scale
        self.alien_vert_speed += self.alien_vert_speedup_scale
        self.bullet_limit += 2
        self.alien_points = int(self.alien_points * self.score_scale)
