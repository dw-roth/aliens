class GameStats:
    """ Track stats during the game """

    def __init__(self, game):
        self.settings = game.settings
        self.reset_stats()
        self.ships_remaining = self.settings.ship_limit - 1
        self.score = 0
        self.high_score = 0

    def reset_stats(self):
        self.ships_remaining = self.settings.ship_limit - 1
        self.score = 0
        self.level = 1
        
