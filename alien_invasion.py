import pygame
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """Klasa służąca jako głowne ogniwo gry"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        pygame.display.set_caption("Alien Invasion")

        self._create_feel()  # tworzymy flote obcych

    def run_game(self):
        """Petla głowna gry"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
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
        self.aliens.draw(self.screen)
        pygame.display.flip()  # odswieza ekran co petle

    def _fire_bullet(self):
        """Pomocnicza sluzaca do wystrzeliwnew_bullet = Bullet(self)
            self.bullets.add(new_bulletania pociskow"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Pomocnicza sluzca do ukatualniania pociskow"""
        self.bullets.update()
        # Usuwamy pociski, ktore wyszly za ekran
        for bullet in self.bullets.copy():
            if bullet.rect.y <= 0:
                self.bullets.remove(bullet)

    def _create_feel(self):
        """Pomocnicza tworzaca flote obcych"""
        new_alien = Alien(self)
        # Ustalenie ile obcych zmiesci sie w jednym wierszu
        available_space_x = self.settings.screen_width - new_alien.rect.width
        number_aliens_x = available_space_x // (2*new_alien.rect.width)
        # Ustalenie liczby wierszy
        available_space_y = self.settings.screen_height - 3*new_alien.rect.height - \
            self.ship.rect.height
        number_aliens_y = available_space_y // (2*new_alien.rect.height)
        # Tworzenie obcych
        for alien_number_y in range(number_aliens_y):
            for alien_number_x in range(number_aliens_x):
                self._create_alien(alien_number_x, alien_number_y)

    def _create_alien(self, alien_number_x, alien_number_y):
        """Pomocnicza tworzaca obcego"""
        new_alien = Alien(self)
        new_alien.x = new_alien.rect.width + 2 * new_alien.rect.width * alien_number_x
        new_alien.rect.x = new_alien.x
        new_alien.y = new_alien.rect.height + 2 * new_alien.rect.height * alien_number_y
        new_alien.rect.y = new_alien.y
        self.aliens.add(new_alien)

    def _update_aliens(self):
        """Pomocnicza sluzca do przesuwania floty"""
        self.aliens.update()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
