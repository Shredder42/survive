import pygame, pygame.font

pygame.font.init()

class Button:
    def __init__(self, message):
        self.message = message
        self.width = 100
        self.height = 25
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 36)

        self.rect = pygame.Rect(1225, 800, self.width, self.height)

        self._prep_message()

    def _prep_message(self):
        self.msg_image = self.font.render(self.message, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self, surface):
        surface.fill(self.button_color, self.rect)
        surface.blit(self.msg_image, self.msg_image_rect)

# btn = Button('roll die')