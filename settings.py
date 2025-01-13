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
        self.bullet_limit = 8

        # alien settings
        self.alien_horiz_speed = 1
        self.alien_vert_speed = 100
        # 1 = moving horizontal to right
        # -1 = moving horizontal to left
        self.fleet_direction = 1

