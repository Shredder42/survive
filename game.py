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
yellow_pieces = make_pieces('yellow', 'yellow_piece.png', 1200, 150)
blue_pieces = make_pieces('blue', 'blue_piece.png', 1200, 250)
green_pieces = make_pieces('green', 'green_piece.png', 1200, 350)

# print(red_pieces)
# for x in red_pieces:
#     print(x.rect)
# print(len(red_pieces))
# yellow_piece = GamePiece('yellow', 6, 'yellow_piece.png', 600, 500)
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

def draw_pieces(pieces):
    for piece in pieces:
        if piece.alive:
            piece.draw(screen, piece.rect)

# def clicked_pieces(pieces, mouse_position):
#     moving_piece = False
#     for idx, piece in enumerate(pieces):
#         if piece.rect.collidepoint(mouse_position):
#             moving_piece = True
#             break
#     return moving_piece, idx
def determine_moving_piece(pieces, mouse_position):
    for idx, piece in enumerate(pieces):
        if piece.rect.collidepoint(mouse_position):
            piece.moving = True
            break
    return idx


# def determine_moving_piece(moving, pieces, index, event):
#     if moving:
#         pieces[index].rect.move_ip(event.rel)
def move_piece(pieces, index, event):
    if index == None:
        pass
    else:
        if pieces[index].moving:
            pieces[index].rect.move_ip(event.rel)

# def stop_moving_piece(moving_piece):
#     moving_piece = False
#     return moving_piece
def stop_moving_piece(pieces, index):
    pieces[index].moving = False
    # return moving_piece

def eat_swimmers(pieces, index, animal):
    if index == None:
        pass
    else:
        if pygame.Rect.colliderect(pieces[index].rect, animal.rect) and not pieces[index].moving:
            pieces[index].alive = False
    # return pieces[idx].alive

# create_game_pieces('red', 0)
# create_game_pieces('yellow', 20)
# create_game_pieces('green', 40)
# create_game_pieces('blue', 60)
# create_game_pieces('maroon', 80)


# moving = False
def main():

    # draw_red = True
    # draw_yellow = True
    red_idx = None
    # moving_red_piece = False
    # moving_red = False
    # moving_yellow = False
    yellow_idx = None
    # moving_yellow_piece = False
    blue_idx = None
    # moving_blue_piece = False
    green_idx = None
    # moving_green_piece = False
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

        draw_pieces(red_pieces)
        draw_pieces(yellow_pieces)
        draw_pieces(blue_pieces)
        draw_pieces(green_pieces)
        # for red_piece in red_pieces:
        #     if red_piece.alive:
        #         red_piece.draw(screen, red_piece.rect)
        # if draw_red:
            # screen.blit(red_piece, red_rect)
            # red_piece.draw(screen, red_piece.rect)
        # if draw_yellow:
            # yellow_piece.draw(screen, yellow_piece.rect)
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

                # if red_piece.rect.collidepoint(pos):
                    # moving_red = True
                # if yellow_piece.rect.collidepoint(pos):
                    # moving_yellow = True

                # red_idx = None
                # for idx, red_piece in enumerate(red_pieces):
                #     if red_piece.rect.collidepoint(pos):
                #         moving_red_piece = True
                #         red_idx = idx

                red_idx = determine_moving_piece(red_pieces, pos)
                yellow_idx = determine_moving_piece(yellow_pieces, pos)
                blue_idx = determine_moving_piece(blue_pieces, pos)
                green_idx = determine_moving_piece(green_pieces, pos)
                # moving_yellow_piece, yellow_idx = clicked_pieces(yellow_pieces, pos)
                # moving_blue_piece, blue_idx = clicked_pieces(blue_pieces, pos)
                # moving_green_piece, green_idx = clicked_pieces(green_pieces, pos)

            elif event.type == pygame.MOUSEMOTION:
                if moving:
                    animals[animal_idx].rect.move_ip(event.rel)
                # if red_idx is not None:
                move_piece(red_pieces, red_idx, event)
                move_piece(yellow_pieces, yellow_idx, event)
                move_piece(blue_pieces, blue_idx, event)
                move_piece(green_pieces, green_idx, event)
                # determine_moving_piece(moving_yellow_piece, yellow_pieces, yellow_idx, event)
                # determine_moving_piece(moving_blue_piece, blue_pieces, blue_idx, event)
                # determine_moving_piece(moving_green_piece, green_pieces, green_idx, event)
                # elif moving_red_piece:
                #     red_pieces[red_idx].rect.move_ip(event.rel)
                # elif moving_red:
                #     red_piece.rect.move_ip(event.rel)
                # if moving_yellow:
                    # yellow_piece.rect.move_ip(event.rel)

            elif event.type == pygame.MOUSEBUTTONUP:
                moving = False
                # moving_red_piece = False
                stop_moving_piece(red_pieces, red_idx)
                stop_moving_piece(yellow_pieces, yellow_idx)
                stop_moving_piece(blue_pieces, blue_idx)
                stop_moving_piece(green_pieces, green_idx)
                # moving_yellow_piece = stop_moving_piece(moving_yellow_piece)
                # moving_blue_piece = stop_moving_piece(moving_blue_piece)
                # moving_green_piece = stop_moving_piece(moving_green_piece)
                # moving_red = False
                # moving_yellow = False

        for animal in animals:
            if animal.eat_swimmers:
                eat_swimmers(red_pieces, red_idx, animal)
                eat_swimmers(yellow_pieces, yellow_idx, animal)
                eat_swimmers(blue_pieces, blue_idx, animal)
                eat_swimmers(green_pieces, green_idx, animal)

                # if red_idx == None:
                #     pass
                # else:
                #     if pygame.Rect.colliderect(red_pieces[red_idx].rect, animal.rect) and not moving_red_piece:
                #         red_pieces[red_idx].alive = False
                # if pygame.Rect.colliderect(red_piece.rect, animal.rect) and not moving_red:
                #     draw_red = False
                # if pygame.Rect.colliderect(yellow_piece.rect, animal.rect) and not moving_yellow:
                    # draw_yellow = False



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


