import pygame
import sys
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Klasa służąca jako głowne ogniwo gry"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.width, self.settings.height))
        self.ship = Ship(self)
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Petla głowna gry"""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Pomocnicza metoda do metody run_game sprawdzajaca dane wejsciowe
            uzytkownika"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.rect.x += 1
                elif event.key == pygame.K_LEFT:
                    self.ship.rect.x -= 1
                elif event.key == pygame.K_UP:
                    self.ship.rect.y -= 1
                elif event.key == pygame.K_DOWN:
                    self.ship.rect.y += 1

    def _update_screen(self):
        """Pomocnicza metoda do metody run_game uakutalniajaca screen """
        self.screen.fill(self.settings.background_color)
        self.ship.show()

        pygame.display.flip()  # odswieza ekran co petle


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
