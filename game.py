import pygame
import math
from random import choice
from tiles import Island, Ocean, Tile
import animals

pygame.init()


SCREEN_WIDTH, SCREEN_HEIGHT = 1350, 1200
OCEAN_BLUE = (43, 101, 236)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# screen.fill(OCEAN_BLUE)
pygame.display.set_caption("SURVIVE!")

def draw_tile(surface, num_sides, tilt_angle, x, y, radius, color):
    pts = []
    for i in range(num_sides):
        x = x + radius * math.cos(tilt_angle + math.pi * 2 * i / num_sides)
        y = y + radius * math.sin(tilt_angle + math.pi * 2 * i / num_sides)
        pts.append((int(x), int(y)))
    return pygame.draw.polygon(surface, color, pts, width = 0)

island = Island()
ocean = Ocean()

whale = animals.Whale()

whales = [animals.Whale() for i in range(5)]
whale_rects = island.return_tile_coords()[0]
sharks = [animals.Shark() for i in range(6)]
shark_rects = island.return_tile_coords()[1]
serpents = [animals.Serpent() for i in range(5)]
# serpent = [animals.Serpent()]
serpents[0].rect.x = 150
serpents[0].rect.y = 105
serpents[1].rect.x = 975
serpents[1].rect.y = 180
serpents[2].rect.x = 540
serpents[2].rect.y = 480
serpents[3].rect.x = 110
serpents[3].rect.y = 780
serpents[4].rect.x = 935
serpents[4].rect.y = 855
serpent_rects = []
for idx, serpent in enumerate(serpents):
    serpent_rects.append(serpent.rect)
    # print(serpent.rect)
# print(serpents)
# print(serpent_rects)
animals = whales + sharks + serpents
animal_rects = whale_rects + shark_rects + serpent_rects
# print(animals)

for idx, animal in enumerate(animals):
    animal.rect.x, animal.rect.y = animal_rects[idx][0], animal_rects[idx][1]

game_pieces = pygame.image.load('game_pieces.png').convert_alpha()
game_pieces = pygame.transform.scale(game_pieces, (100, 50))
red_piece = game_pieces.subsurface(0, 0, 20, 50)
red_rect = red_piece.get_rect()
red_rect.x = 500
red_rect.y = 500
print(red_rect)
yellow_piece = game_pieces.subsurface(20, 0, 20, 50)
yellow_rect = yellow_piece.get_rect()
yellow_rect.x = 700
yellow_rect.y = 700
print(yellow_rect)

# moving = False
def main():

    moving_red = False
    moving = False
    run = True

    # i = 0
    # for item in whales:
    #     item.draw(screen, whale_rects[i])
    #     i += 1

    while run:

        screen.fill(OCEAN_BLUE)
        # whales[0].draw(screen, whales[0].rect)
        for animal in animals:
            animal.draw(screen, animal.rect)
        # for shark in sharks:
        #     shark.draw(screen, shark.rect)

        # screen.blit(whale.image, whale.rect)
        # draw_tile(screen, 6, math.pi / 6, 0, 0, 50, RED)

        ocean_rects = []
        ocean_drawn_tiles = []
        for tile in ocean.tiles:
                ocean_rects.append(tile.draw(screen, width = 1))
                ocean_drawn_tiles.append(tile)

        island_rects = []
        island_drawn_tiles = []
        for tile in island.tiles:
            idx = 0
            count = 100
            if not tile.sunk:
                island_rects.append(tile.draw(screen))
                island_drawn_tiles.append(tile)
            # if tile.backside == 'add whale':
            #     screen.blit(whales[idx].image, (count, count))
            #     count += 100
            #     idx += 1
            #     whales.pop()


        island_tile_rects = zip(island_drawn_tiles, island_rects)

        screen.blit(red_piece, red_rect)

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
                        # pygame.draw.polygon(screen, OCEAN_BLUE, island_tile.coordinates) # why do I need this?
                        ocean.tiles.append(Tile(BLACK, island_tile.coordinates))
                        # if island_tile.backside == 'add whale':
                        #     whale.draw(screen, (island_rect.left + 15, island_rect.top + 15))
                        # elif island_tile.backside == 'add shark':
                        #     shark = animals.Shark((island_rect.left + 15, island_rect.top + 15))
                        #     shark.draw(screen)

                # whale.move(screen, pos)
                # whale.selected = False
                # print(whale.selected)

                if whale.rect.collidepoint(pos):
                    moving = True
                    # whale.selected = True
                    # print(whale.selected)

                # if whales[0].rect.collidepoint(pos):
                #     moving = True
                #     print('whale 0 selected')

                animal_idx = None
                for idx, item in enumerate(animals):
                    if item.rect.collidepoint(pos):
                        moving = True
                        animal_idx = idx

                if red_rect.collidepoint(pos):
                    moving_red = True

            elif event.type == pygame.MOUSEBUTTONUP:
                moving = False
                moving_red = False
                # print(moving)

            elif event.type == pygame.MOUSEMOTION and moving:
                # whale.rect.move_ip(event.rel)
                animals[animal_idx].rect.move_ip(event.rel)
            elif event.type == pygame.MOUSEMOTION and moving_red:
                red_rect.move_ip(event.rel)

        # whale.draw(screen, whale.rect)


                # if whale.selected:
                #     whale.draw(screen, (pos))
                #     whale.selected = False

        pygame.display.update()

    pygame.quit()
    print(len(ocean_drawn_tiles))
    print(len(island_drawn_tiles))

if __name__ == '__main__':
    main()


