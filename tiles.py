import math
from random import choice


class Tile:
    def __init__(self, color, backside, outline):
        self.color = color
        # self.coordinates = self.coordinates
        self.backside = backside
        self.outline = outline
        self.sunk = False

    def show(self):
        print(self.color, self.backside, self.outline, self.sunk)

class Deck:
    def __init__(self):
        self.tiles = []
        self.build()
        self.coordinates = []
        # colors
        self.beach_brown = (255, 218, 180)
        self.forest_green = (63, 90, 54)
        self.rocky_gray = (94, 107, 108)
        self.ocean_blue = (43, 101, 236)
        self.tile_colors = [beach_brown, forest_green, rocky_gray]
        # with radius = 50
        self.radius = 50
        self.tile_width = 50 / math.tan(math.pi / 6)
        self.tile_height = 100
        self.self.tile_tip_dist = 150
        self.island_rows = [4, 5, 8, 7, 8, 5, 4]



    def __tile_specs(self, num_sides, tilt_angle, x, y, radius):
        pts = []
        for i in range(num_sides):
            x = x + radius * math.cos(tilt_angle + math.pi * 2 * i / num_sides)
            y = y + radius * math.sin(tilt_angle + math.pi * 2 * i / num_sides)
            pts.append((int(x), int(y)))
        return pts


for idx, island_row in enumerate(self.island_rows):
# functionalize these?
    if idx == 0:
        for i in range(island_row):
            tiles.append(tile_specs(6, math.pi / 6, 5 * self.tile_width + i * self.tile_width, 100 + self.self.tile_tip_dist, 50))
    elif idx == 1:
        for i in range(island_row):
            tiles.append(tile_specs(6, math.pi / 6, 4.5 * self.tile_width + i * self.tile_width, 25 + self.self.tile_tip_dist * 2, 50))
    elif idx == 2:
        for i in range(island_row):
            tiles.append(tile_specs(6, math.pi / 6, 3 * self.tile_width + i * self.tile_width, 100 + self.self.tile_tip_dist * 2, 50))
    elif idx == 3:
        for i in range(3): # open space in middle
            tiles.append(tile_specs(6, math.pi / 6, 3.5 * self.tile_width + i * self.tile_width, 25 + self.self.tile_tip_dist * 3, 50))
        for i in range(4, island_row):
            tiles.append(tile_specs(6, math.pi / 6, 3.5 * self.tile_width + i * self.tile_width, 25 + self.self.tile_tip_dist * 3, 50))
    elif idx == 4:
        for i in range(island_row):
            tiles.append(tile_specs(6, math.pi / 6, 3 * self.tile_width + i * self.tile_width, 100 + self.self.tile_tip_dist * 3, 50))
    elif idx == 5:
        for i in range(island_row):
            tiles.append(tile_specs(6, math.pi / 6, 4.5 * self.tile_width + i * self.tile_width, 25 + self.self.tile_tip_dist * 4, 50))
    else:
        for i in range(island_row):
            tiles.append(tile_specs(6, math.pi / 6, 5 * self.tile_width + i * self.tile_width, 100 + self.self.tile_tip_dist * 4, 50))



    def build(self):
        '''Creates all the tiles'''
        for i in range(3):
            self.tiles.append(Tile(beach_brown, 'add whale', 'green'))
        for i in range(3):
            self.tiles.append(Tile(beach_brown, 'add shark', 'green'))
        self.tiles.append(Tile(beach_brown, 'add boat', 'green'))
        for i in range(3):
            self.tiles.append(Tile(beach_brown, 'dolphin ride', 'red'))
        for i in range(2):
            self.tiles.append(Tile(beach_brown, 'favorable winds', 'red'))
        self.tiles.append(Tile(beach_brown, 'move whale', 'red'))
        self.tiles.append(Tile(beach_brown, 'move shark', 'red'))
        self.tiles.append(Tile(beach_brown, 'move serpent', 'red'))
        self.tiles.append(Tile(beach_brown, 'remove shark', 'red'))
        for i in range(3):
            self.tiles.append(Tile(forest_green, 'add boat', 'green'))
        for i in range(2):
            self.tiles.append(Tile(forest_green, 'add whale', 'green'))
        for i in range(2):
            self.tiles.append(Tile(forest_green, 'add shark', 'green'))
        for i in range(2):
            self.tiles.append(Tile(forest_green, 'whirlpool', 'green'))
        for i in range(2):
            self.tiles.append(Tile(forest_green, 'remove whale', 'red'))
        self.tiles.append(Tile(forest_green, 'remove shark', 'red'))
        self.tiles.append(Tile(forest_green, 'move whale', 'red'))
        self.tiles.append(Tile(forest_green, 'move shark', 'red'))
        self.tiles.append(Tile(forest_green, 'move serpent', 'red'))
        self.tiles.append(Tile(forest_green, 'dolphin ride', 'red'))
        for i in range(4):
            self.tiles.append(Tile(rocky_gray, 'whirlpool', 'green'))
        self.tiles.append(Tile(rocky_gray, 'add shark', 'green'))
        self.tiles.append(Tile(rocky_gray, 'volcano', 'green'))
        self.tiles.append(Tile(rocky_gray, 'remove whale', 'red'))
        self.tiles.append(Tile(rocky_gray, 'remove shark', 'red'))


    def show(self):
        for t in self.tiles:
            t.show()

deck = Deck()
deck.show()

