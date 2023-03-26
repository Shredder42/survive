import pygame
import math
from random import choice
from tiles import Island
from tiles import Ocean
from tiles import Tile
import animals


SCREEN_WIDTH, SCREEN_HEIGHT = 1350, 1200
OCEAN_BLUE = (43, 101, 236)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(OCEAN_BLUE)
pygame.display.set_caption("SURVIVE! Game Board")

island = Island()
ocean = Ocean()

def main():
    run = True

    while run:

        ocean_rects = []
        ocean_drawn_tiles = []
        for tile in ocean.tiles:
                ocean_rects.append(tile.draw(screen, width = 1))
                ocean_drawn_tiles.append(tile)

        island_rects = []
        island_drawn_tiles = []
        for tile in island.tiles:
            if not tile.sunk:
                island_rects.append(tile.draw(screen))
                island_drawn_tiles.append(tile)

        island_tile_rects = zip(island_drawn_tiles, island_rects)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                for island_tile, island_rect in island_tile_rects:
                    if island_rect.collidepoint((pos)):
                        print(island_tile.backside)
                        island_tile.sunk = True
                        pygame.draw.polygon(screen, OCEAN_BLUE, island_tile.coordinates) # why do I need this?
                        ocean.tiles.append(Tile(BLACK, island_tile.coordinates))
                        if island_tile.backside == 'add whale':
                            whale = animals.Whale((island_rect.left + 15, island_rect.top + 15))
                            whale.draw(screen)
                        if island_tile.backside == 'add shark':
                            shark = animals.Shark((island_rect.left + 15, island_rect.top + 15))
                            shark.draw(screen)



        pygame.display.update()

    pygame.quit()
    print(len(ocean_drawn_tiles))
    print(len(island_drawn_tiles))

if __name__ == '__main__':
    main()


