import pygame
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """Klasa służąca jako głowne ogniwo gry"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Petla głowna gry"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullet()
            self._update_screen()

    def _check_events(self):
        """Pomocnicza metoda do metody run_game sprawdzajaca dane wejsciowe
            uzytkownika"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keyup_events(self, event):
        """Reakcja na nacisniecia klawisza"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_keydown_events(self, event):
        """Reakcja na zwoleninie klawisza"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_ESCAPE:
            sys.exit()

    def _update_screen(self):
        """Pomocnicza metoda do metody run_game uakutalniajaca screen """
        self.screen.fill(self.settings.background_color)
        self.ship.show()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()  # odswieza ekran co petle

    def _fire_bullet(self):
        """Pomocnicza sluzaca do wystrzeliwnew_bullet = Bullet(self)
            self.bullets.add(new_bulletania pociskow"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullet(self):
        """Pomocnicza sluzca do ukatualniania pociskow"""
        self.bullets.update()
        # Usuwamy pociski, ktore wyszly za ekran
        for bullet in self.bullets.copy():
            if bullet.rect.y <= 0:
                self.bullets.remove(bullet)


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
