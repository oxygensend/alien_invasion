import pygame.font


class Button:
    """Klasa sluzaca do budowy przycisku"""

    def __init__(self, msg, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Wymiary
        self.width, self.height = 210, 80
        self.button_color = (21, 116, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Tworzenie prostokata
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Metoda konwertujaca tekst na obrazek"""

        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)  # Zmienia tekst przechowywany w msg na obraz
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_msg(self, y1=0, y2=0):
        """Metoda rysujaca przycisk z tekstem"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def move_button(self, self2):
        """Metoda umozliwiajaca przesuwanie przycisku"""
        self.rect = pygame.Rect.move(self2.rect, 0, 82)
        self.msg_image_rect.center = self.rect.center
