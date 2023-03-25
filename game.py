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

def main():
    run = True

    while run:

        rects = []
        drawn_tiles = []
        for tile in island.tiles:
            if not tile.sunk:
                rects.append(tile.draw(screen))
                drawn_tiles.append(tile)

        tile_rects = zip(drawn_tiles, rects)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
                pos = pygame.mouse.get_pos()

                for tile, rect in tile_rects:
                    if rect.collidepoint((pos)):
                        print(tile.backside)
                        tile.sunk = True
                        pygame.draw.polygon(screen, OCEAN_BLUE, tile.coordinates)


        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()
    # print(island_tiles)
    # print(len(island_tiles))
