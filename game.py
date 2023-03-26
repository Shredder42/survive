import pygame
import math
from random import choice
from tiles import Island
from tiles import Ocean
import animals


SCREEN_WIDTH, SCREEN_HEIGHT = 1350, 1200
OCEAN_BLUE = (43, 101, 236)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(OCEAN_BLUE)
pygame.display.set_caption("SURVIVE! Game Board")

island = Island()
ocean = Ocean()

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

        for tile in ocean.tiles:
            tile.draw(screen, width= 1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                for tile, rect in tile_rects:
                    if rect.collidepoint((pos)):
                        print(tile.backside)
                        tile.sunk = True
                        pygame.draw.polygon(screen, OCEAN_BLUE, tile.coordinates)
                        if tile.backside =='add whale':
                            whale = animals.Whale((rect.left + 15, rect.top + 15))
                            whale.draw(screen)
                        if tile.backside =='add shark':
                            shark = animals.Shark((rect.left + 15, rect.top + 15))
                            shark.draw(screen)



        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()

