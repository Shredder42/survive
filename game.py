import pygame
import math
from random import choice
from tiles import Deck

SCREEN_WIDTH, SCREEN_HEIGHT = 1350, 1200
OCEAN_BLUE = (43, 101, 236)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(OCEAN_BLUE)
pygame.display.set_caption("SURVIVE! Game Board")

island = Deck()
print(type(island))
island_tiles = []
for tile in island.tiles:
    island_tiles.append((tile.color, tile.coordinates))


def draw_tiles(surface, island_tiles):
    for tile in island_tiles:
        pygame.draw.polygon(surface, tile[0], tile[1])

def main():
    run = True
    sunk = False

    while run:

        if not sunk:
            draw_tiles(screen, island_tiles)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.MOUSEBUTTONDOWN:
                sunk = True
                # drawRegularPolygon(screen, OCEAN_BLUE, 6, 0, 500, 500, 50)
                print(pygame.mouse.get_pos())


        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()
