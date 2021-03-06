import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """Klasa przeznaczona do zarzadzania statkiem kosmicznym"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Wczytanie obrazu statku
        self.image = pygame.image.load('alien_game/images/ship.bmp')
        self.rect = self.image.get_rect()  # pozycja obrazu

        self.center_ship()

        # Poruszanie sie w kierunkach
        self.moving_right = False
        self.moving_left = False

    def show(self):
        """Metoda wyswietlajaca statek"""

        self.screen.blit(self.image, self.rect)

    def update(self):
        """Metoda umożliwiająca ruch statku"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def center_ship(self):
        """Metoda wysrodkowujaca statek"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
