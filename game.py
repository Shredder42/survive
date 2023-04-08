import pygame
import math
from random import choice
from tiles import Island, Ocean, Tile
from game_pieces import GamePiece, create_game_pieces
import animals

pygame.init()


SCREEN_WIDTH, SCREEN_HEIGHT = 1350, 1200
OCEAN_BLUE = (43, 101, 236)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
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
red_piece = GamePiece('red', 6, 'red_piece.png', 400, 800)
# print(red_piece.rect)
# red_piece.rect.x = 400
# red_piece.rect.y = 800
print(red_piece.rect)

def make_pieces(color, png, start_x, start_y):
    pieces = []
    for i in range(10):
        if i < 3:
            value = 1
        elif i < 5:
            value = 2
        elif i < 7:
            value = 3
        elif i == 7:
            value = 4
        elif i == 8:
            value = 5
        elif i == 9:
            value = 6

        if i < 5:
            pieces.append(GamePiece(color, value, png, start_x + 30 * i, start_y))
        else:
            pieces.append(GamePiece(color, value, png, start_x + 30 * (i - 5), start_y + 50))
    return pieces


red_pieces = make_pieces('red', 'red_piece.png', 1200, 50)
print(red_pieces)
for x in red_pieces:
    print(x.rect)
print(len(red_pieces))
yellow_piece = GamePiece('yellow', 6, 'yellow_piece.png', 600, 500)
# yellow_piece.rect.x = 600
# yellow_piece.rect.y = 500

# def create_animals(animal, num_of_animals, island, initial_rects = None):
#         return [animals.animal for i in range(num_of_animals)], island.return_tile_coords() [0]

# whales = create_animals(Whale(), 5, island)[0]
whales = [animals.Whale() for i in range(5)]
whale_rects = island.return_tile_coords()[0]
sharks = [animals.Shark() for i in range(6)]
shark_rects = island.return_tile_coords()[1]
serpents = [animals.Serpent() for i in range(5)]
serpent_initial_rects = [(150, 105), (975, 180), (540, 480), (110, 780), (935, 855)]

def set_initial_serpent_rects(serpents, serpent_initial_rects):
    serpent_rects = []
    for idx, serpent in enumerate(serpents):
        serpent.rect.x = serpent_initial_rects[idx][0]
        serpent.rect.y = serpent_initial_rects[idx][1]
        serpent_rects.append(serpent.rect)
    return serpent_rects
serpent_rects = set_initial_serpent_rects(serpents, serpent_initial_rects)

animals = whales + sharks + serpents
animal_rects = whale_rects + shark_rects + serpent_rects
# print(animals)

for idx, animal in enumerate(animals):
    animal.rect.x, animal.rect.y = animal_rects[idx][0], animal_rects[idx][1]

# create_game_pieces('red', 0)
# create_game_pieces('yellow', 20)
# create_game_pieces('green', 40)
# create_game_pieces('blue', 60)


# moving = False
def main():

    draw_red = True
    draw_yellow = True
    red_idx = None
    moving_red_piece = False
    moving_red = False
    moving_yellow = False
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

        for red_piece in red_pieces:
            if red_piece.alive:
                red_piece.draw(screen, red_piece.rect)
        if draw_red:
            # screen.blit(red_piece, red_rect)
            red_piece.draw(screen, red_piece.rect)
        if draw_yellow:
            yellow_piece.draw(screen, yellow_piece.rect)
        # screen.blit(yellow_piece, yellow_rect)

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

                # if whale.rect.collidepoint(pos):
                #     moving = True
                    # whale.selected = True
                    # print(whale.selected)

                # if whales[0].rect.collidepoint(pos):
                #     moving = True
                #     print('whale 0 selected')

                animal_idx = None
                for idx, animal in enumerate(animals):
                    if animal.rect.collidepoint(pos):
                        moving = True
                        animal_idx = idx

                if red_piece.rect.collidepoint(pos):
                    moving_red = True
                if yellow_piece.rect.collidepoint(pos):
                    moving_yellow = True

                # red_idx = None
                for idx, red_piece in enumerate(red_pieces):
                    if red_piece.rect.collidepoint(pos):
                        moving_red_piece = True
                        red_idx = idx

            elif event.type == pygame.MOUSEMOTION:
                if moving:
                    animals[animal_idx].rect.move_ip(event.rel)
                elif moving_red_piece:
                    red_pieces[red_idx].rect.move_ip(event.rel)
                elif moving_red:
                    red_piece.rect.move_ip(event.rel)
                elif moving_yellow:
                    yellow_piece.rect.move_ip(event.rel)

            elif event.type == pygame.MOUSEBUTTONUP:
                moving = False
                moving_red_piece = False
                moving_red = False
                moving_yellow = False

        for animal in animals:
            if animal.eat_swimmers:
                if red_idx == None:
                    pass
                else:
                    if pygame.Rect.colliderect(red_pieces[red_idx].rect, animal.rect) and not moving_red_piece:
                        red_pieces[red_idx].alive = False
                    pass
                if pygame.Rect.colliderect(red_piece.rect, animal.rect) and not moving_red:
                    draw_red = False
                if pygame.Rect.colliderect(yellow_piece.rect, animal.rect) and not moving_yellow:
                    draw_yellow = False



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


