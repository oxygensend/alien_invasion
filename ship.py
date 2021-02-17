import pygame


class Ship:
    """Klasa przeznaczona do zarzadzania statkiem kosmicznym"""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Wczytanie obrazu statku
        self.image = pygame.image.load('alien_game/images/ship.bmp')
        self.rect = self.image.get_rect()  # pozycja obrazu

        self.rect.midbottom = self.screen_rect.midbottom

    def show(self):
        """Metoda wyswietlajaca statek"""

        self.screen.blit(self.image, self.rect)
