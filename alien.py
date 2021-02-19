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

    def check_edge(self):
        """ Zwraca prawde jezeli kosmita znajdue sie na krawedzi ekranu """
        if self.rect.left <= 0 or self.rect.right >= self.screen.get_rect().right:
            return True

    def update(self):
        """Uaktualnia pozycja obcego w osi x """
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
