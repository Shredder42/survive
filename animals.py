import pygame

class Whale:
    def __init__(self, coordinates):
        self.movement = 3
        self.action = 'capsize boat'
        self.coordinates = coordinates
        self.image = self.load_image()
        self.rect = self.image.get_rect() # new, see if this works

    def load_image(self):
        image = pygame.image.load('whale.png').convert_alpha()
        image = pygame.transform.scale(image, (50, 50))
        return image

    def draw(self, surface):
        return surface.blit(self.image, self.coordinates)

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

    def draw(self, surface):
        surface.blit(self.image, self.coordinates)



