
class Settings:
    """Klasa przechowujaca wszystkie ustawienia gry"""

    def __init__(self):
        # ustawienia okna
        self.screen_width = 1200
        self.screen_height = 800
        self.background_color = (230, 230, 230)

        # ustawienia statku
        self.ship_speed = 1.5
        self.ships_limit = 3

        # ustawienia pociskow
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        # ustawienia kosmitow
        self.alien_speed = 1.0
        self.fleet_direction = 1  # 1 prawo -1 lewo
        self.fleet_drop_speed = 10  # predkosc z jaka obcy beda zmninieac rzad

        # zmienna zwiekszajaca poziom rozgrywki
        self.speedup_scale = 1.1

    def reset_speed(self):
        self.bullet_speed = 1.5
        self.ship_speed = 1.5
        self.alien_speed = 1.0

    def increase_speed(self):
        self.bullet_speed *= self.speedup_scale
        self.ship_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
