class GameStats:
    """ Track stats during the game """

    def __init__(self, game):
        self.settings = game.settings
        self._reset_stats()

    def _reset_stats(self):
        self.ships_remaining = self.settings.ship_limit
