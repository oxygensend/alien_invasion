class GameStats:
    """Monitorowanie danych statysycznych w calej grze"""

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        self.lvl_menu = False

    def reset_stats(self):
        self.ships_left = self.settings.ships_limit
