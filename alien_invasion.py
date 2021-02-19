import pygame
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from time import sleep
from game_stats import GameStats
from button import Button


class AlienInvasion:
    """Klasa służąca jako głowne ogniwo gry"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        self.play_button = Button("Play", self)
        self.quit_button = Button("Quit", self)
        self.stats = GameStats(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        pygame.display.set_caption("Alien Invasion")

        self._create_feel()  # tworzymy flote obcych

    def run_game(self):
        """Petla głowna gry"""
        while True:
            self._check_events()

            if self.stats.game_active:
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_button_play(pygame.mouse.get_pos())
                self._check_button_quit(pygame.mouse.get_pos())
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_button_play(self, mouse_pos):
        """Metoda odpalajaca gre przez klikniecie"""
        if self.play_button.rect.collidepoint(mouse_pos) and \
                not self.stats.game_active:
            self._start_game()

    def _check_button_quit(self, mouse_pos):
        """Metoda umożliwiajaca wyjscie z gry przez przycisk"""
        if self.quit_button.rect.collidepoint(mouse_pos) and \
                not self.stats.game_active:
            sys.exit()

    def _start_game(self):
        """Metoda pozwalajaca na urchumienie gry"""
        self.stats.reset_stats()
        self.settings.reset_speed()
        self.stats.game_active = True

        self.aliens.empty()
        self.bullets.empty()

        self._create_feel()
        self.ship.center_ship()

        # ukrycie przycisku myszy
        pygame.mouse.set_visible(False)

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
        elif event.key == pygame.K_g:
            self._start_game()

    def _update_screen(self):
        """Pomocnicza metoda do metody run_game uakutalniajaca screen """
        self.screen.fill(self.settings.background_color)
        self.ship.show()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        if not self.stats.game_active:
            # Button - game
            self.play_button.draw_msg()
            # Button - quit
            self.quit_button.rect = pygame.Rect.move(self.play_button.rect, 0, 82)
            self.quit_button.msg_image_rect.center = self.quit_button.rect.center
            self.quit_button.draw_msg()

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

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Pomocnicza sprawdzajaca kolizje floty z pociskami"""
        # sprite.groupcollide(obiekt1ktorysiepokrywa, obiek2ktorysiepoktywa
        # czy 1 ma zostac usuniety, czy 2 ma zostacusuniety)
        # metoda sprawdza czy dane obiekty sie pokrywaja i zwraca slownik
        # gdzie klucz to 1 argument wartosc 2
        pygame.sprite.groupcollide(self.bullets,
                                   self.aliens, True, True)
        if not self.aliens:
            self.bullets.empty()
            self._create_feel()
            self.settings.increase_speed()

    def _check_screen_alien_collisions(self):
        """Pomocnicza sprawdzajaca kolizje kosmity z krawedzia ekranu"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.screen.get_rect().bottom:
                self._hit_ship()
                break

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

    def _change_fleet_direction(self):
        """"Przesuwa cala linie floty w dol"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_fleet_edge(self):
        """Odpowiednia reakcja gdy flota dotrze do krawedzi"""
        for alien in self.aliens.sprites():
            if alien.check_edge():
                self._change_fleet_direction()
                break

    def _update_aliens(self):
        """Pomocnicza sluzca do przesuwania floty"""
        self._check_fleet_edge()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._hit_ship()

        self._check_screen_alien_collisions()

    def _hit_ship(self):
        """Pomocnicza rozpoczyna gre od nowa gdy nastąpi kolizja
            statku z kosmita """

        if self.stats.ships_left > 1:
            self.stats.ships_left -= 1
            self.bullets.empty()
            self.aliens.empty()
            self._create_feel()
            self.ship.center_ship()
            sleep(1)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
