import pygame.image


class Settings:
    """Klasa przechowujaca wszystkie ustawienia gry"""

    def __init__(self):
        # ustawienia okna
        self.screen_width = 1200
        self.screen_height = 800
        self.background_color = (230, 230, 230)
        self.bg_image = pygame.image.load('alien_game/images/space.jpg')
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
        self.alien_score = 50
        # zmienna zwiekszajaca poziom rozgrywki
        self.speedup_scale = 1.1

    def reset_speed(self):
        self.bullet_speed = 1.5
        self.ship_speed = 1.5
        self.alien_speed = 1.0
        self.alien_score = 50

    def increase_speed(self, speed_up=None, score_scale=1):
        speed_up = self.speedup_scale if speed_up is None else speed_up
        self.bullet_speed *= speed_up
        self.ship_speed *= speed_up
        self.alien_speed *= speed_up
        self.alien_score = int(self.alien_score * score_scale)
