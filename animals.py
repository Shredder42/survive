import pygame

class Whale:
    def __init__(self, coordinates):
        self.movement = 3
        self.action = 'capsize boat'
        self.coordinates = coordinates
        self.image = self.load_image()

    def load_image(self):
        image = pygame.image.load('whale.png').convert_alpha()
        image = pygame.transform.scale(image, (50, 50))
        return image

    def draw(self, surface):
        surface.blit(self.image, self.coordinates)

class Shark:
    def __init__(self, coordinates):
        self.movement = 3
        self.action = 'eat swimmers'
        self.coordinates = coordinates
        self.image = self.load_image()

    def load_image(self):
        image = pygame.image.load('sharkfin2.png').convert_alpha()
        image = pygame.transform.scale(image, (70, 70))
        return image

    def draw(self, surface):
        surface.blit(self.image, self.coordinates)



