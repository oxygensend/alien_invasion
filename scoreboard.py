import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scoreboard:
    """Klasa odpowiedzialna za wyswietlanie postepow w grze"""

    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.stats = ai_game.stats
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Metoda przeksztalcajaca tekst na obraz"""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str,
                                            True, self.text_color,
                                            self.settings.background_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Metoda przeksztalcajaca najwyzszy dotychczasowy wynik"""
        rounded_score = round(self.stats.high_score, -1)
        score_str = "{:,}".format(rounded_score)
        self.high_score_image = self.font.render(score_str,
                                                 True, self.text_color,
                                                 self.settings.background_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.midtop = self.screen_rect.midtop
        self.high_score_rect.top = 20

    def prep_level(self):
        """Metoda przeksztalcajaca lvl na obraz kekw"""
        self.lvl_image = self.font.render(str(self.stats.level), True,
                                          self.text_color, self.settings.background_color)
        self.lvl_image_rect = self.lvl_image.get_rect()
        self.lvl_image_rect.right = self.screen_rect.right - 20
        self.lvl_image_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """Metoda wyswietla ilosc statkow"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        """Metoda wyswietlajaca ilosc punktow"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.lvl_image, self.lvl_image_rect)
        self.ships.draw(self.screen)

    def check_high_score(self):
        """Sprawdzenie czy mamy nowy rekord gry"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
