import json


class GameStats:
    """Monitorowanie danych statysycznych w calej grze"""

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        self.lvl_menu = False
        self.lvl_choosen = False
        self.warning_menu = False
        self.level = 1
        try:
            with open('alien_game/high_score.json') as high_score_file:
                self.high_score = json.load(high_score_file)
        except IOError:
            self.high_score = 0

    def reset_stats(self):
        self.ships_left = self.settings.ships_limit
        self.score = 0
