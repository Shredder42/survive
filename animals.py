import pygame
# import game
import tiles

class Whale:
    def __init__(self, coordinates):
        self.movement = 3
        self.capsize_boat = True
        self.eat_swimmers = False
        self.coordinates = coordinates
        self.image = self.load_image()
        self.selected = False
        self.rect = self.image.get_rect()
        self.rect.x = self.coordinates[0]
        self.rect.y = self.coordinates[1]

    def load_image(self):
        image = pygame.image.load('whale.png').convert_alpha()
        image = pygame.transform.scale(image, (50, 50))
        return image

    def draw(self, surface):
        return surface.blit(self.image, self.rect)

    def show_selected(self):
        return self.selected

class Shark:
    def __init__(self):
        self.movement = 2
        self.capsize_boat = False
        self.eat_swimmers = True
        # self.coordinates = coordinates
        self.image = self.load_image()
        self.rect = self.image.get_rect()

    def load_image(self):
        image = pygame.image.load('sharkfin2.png').convert_alpha()
        image = pygame.transform.scale(image, (70, 70))
        return image

    def draw(self, surface, coords):
        self.rect.x = coords[0]
        self.rect.y = coords[1]
        return surface.blit(self.image, coords)

class Serpent:
    def __init__(self):
        self.movement = 1
        self.capsize_boat = True
        self.eat_swimmers = True
        self.image = self.load_image()
        self.rect = self.image.get_rect()

    def load_image(self):
        image = pygame.image.load('sea_serpent.png').convert_alpha()
        image = pygame.transform.scale(image, (50, 50))
        return image

    def draw(self, surface, coords):
        self.rect.x = coords[0]
        self.rect.y = coords[1]
        return surface.blit(self.image, coords)





