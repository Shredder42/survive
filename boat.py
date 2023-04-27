import pygame

class Boat:
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.image = self.load_image()
        self.rect =self.image.get_rect()
        self.rect.x = self.coordinates[0]
        self.rect.y = self.coordinates[1]
        self.moving = False

    def load_image(self):
        image = pygame.image.load('boat.png').convert_alpha()
        image = pygame.transform.scale(image, (50, 50))
        return image

    def draw(self, surface):
        return surface.blit(self.image, self.rect)