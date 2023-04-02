import pygame
# import game
import tiles

class Whale:
    def __init__(self):
        self.movement = 3
        self.action = 'capsize boat'
        # self.coordinates = coordinates
        self.image = self.load_image()
        self.selected = False
        self.rect = self.image.get_rect()

    def load_image(self):
        image = pygame.image.load('whale.png').convert_alpha()
        image = pygame.transform.scale(image, (50, 50))
        return image

    def draw(self, surface, coords):
        self.rect.x = coords[0]
        self.rect.y = coords[1]
        return surface.blit(self.image, coords)

    def show_selected(self):
        return self.selected



    # def get_rect(self):
    #     return self.image.get_rect()

class Shark:
    def __init__(self, coordinates):
        self.movement = 2
        self.action = 'eat swimmers'
        self.coordinates = coordinates
        self.image = self.load_image()

    def load_image(self):
        image = pygame.image.load('sharkfin2.png').convert_alpha()
        image = pygame.transform.scale(image, (70, 70))
        return image

    def draw(self, surface, coords):
        self.rect.x = coords[0]
        self.rect.y = coords[1]
        return surface.blit(self.image, coords)



