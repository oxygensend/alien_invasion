import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Klasa odwzorowujaca obecego"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load("alien_game/images/alien.bmp")
        self.rect = self.image.get_rect()

        # ustawiamy kazdego nowego obcego w lewym gornym rogu
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def update(self):
        self.x += self.settings.alien_speed
        self.rect.x = self.x
