
class Settings:
    def __init__(self):
        # ustawienia okna
        self.screen_width = 1200
        self.screen_height = 800
        self.background_color = (230, 230, 230)

        # ustawienia statku
        self.ship_speed = 1.5

        # ustawienia pociskow
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        # ustawienia kosmitow
        self.alien_speed = 1.0
        self.feel_direction = 1
