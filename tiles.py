import math
from random import choice


class Tile:
    def __init__(self, color, coordinates, backside, outline):
        self.color = color
        self.coordinates = coordinates
        self.backside = backside
        self.outline = outline
        self.sunk = False

    def show(self):
        print(self.color, self.coordinates, self.backside, self.outline, self.sunk)

class Deck:
    def __init__(self):
        self.tiles = []
        self.beach_brown = (255, 218, 180)
        self.coordinates = []
        # colors
        self.beach_brown = (255, 218, 180)
        self.forest_green = (63, 90, 54)
        self.rocky_gray = (94, 107, 108)
        self.ocean_blue = (43, 101, 236)
        self.tile_colors = [self.beach_brown, self.forest_green, self.rocky_gray]
        # with radius = 50
        self.radius = 50
        self.tile_width = 50 / math.tan(math.pi / 6)
        self.tile_height = 100
        self.tile_tip_dist = 150
        self.island_rows = [4, 5, 8, 7, 8, 5, 4]

        self.build()


    def _tile_specs(self, num_sides, tilt_angle, x, y, radius):
        pts = []
        for i in range(num_sides):
            x = x + radius * math.cos(tilt_angle + math.pi * 2 * i / num_sides)
            y = y + radius * math.sin(tilt_angle + math.pi * 2 * i / num_sides)
            pts.append((int(x), int(y)))
        return pts


    def _generate_island_coordinates(self):
        for idx, island_row in enumerate(self.island_rows):
            if idx == 0:
                for i in range(island_row):
                    self.coordinates.append(self._tile_specs(6, math.pi / 6, 5 * self.tile_width + i * self.tile_width, 100 + self.tile_tip_dist, self.radius))
            elif idx == 1:
                for i in range(island_row):
                    self.coordinates.append(self._tile_specs(6, math.pi / 6, 4.5 * self.tile_width + i * self.tile_width, 25 + self.tile_tip_dist * 2, self.radius))
            elif idx == 2:
                for i in range(island_row):
                    self.coordinates.append(self._tile_specs(6, math.pi / 6, 3 * self.tile_width + i * self.tile_width, 100 + self.tile_tip_dist * 2, self.radius))
            elif idx == 3:
                for i in range(3): # open space in middle
                    self.coordinates.append(self._tile_specs(6, math.pi / 6, 3.5 * self.tile_width + i * self.tile_width, 25 + self.tile_tip_dist * 3, self.radius))
                for i in range(4, island_row):
                    self.coordinates.append(self._tile_specs(6, math.pi / 6, 3.5 * self.tile_width + i * self.tile_width, 25 + self.tile_tip_dist * 3, self.radius))
            elif idx == 4:
                for i in range(island_row):
                    self.coordinates.append(self._tile_specs(6, math.pi / 6, 3 * self.tile_width + i * self.tile_width, 100 + self.tile_tip_dist * 3, self.radius))
            elif idx == 5:
                for i in range(island_row):
                    self.coordinates.append(self._tile_specs(6, math.pi / 6, 4.5 * self.tile_width + i * self.tile_width, 25 + self.tile_tip_dist * 4, self.radius))
            else:
                for i in range(island_row):
                    self.coordinates.append(self._tile_specs(6, math.pi / 6, 5 * self.tile_width + i * self.tile_width, 100 + self.tile_tip_dist * 4, self.radius))

    def _select_coordinates(self):
        coord = choice(self.coordinates)
        self.coordinates.remove(coord)
        return coord

    def build(self):
        '''Creates all the tiles'''
        self._generate_island_coordinates()
        for i in range(3):
            self.tiles.append(Tile(self.beach_brown, self._select_coordinates(), 'add whale', 'green'))
        for i in range(3):
            self.tiles.append(Tile(self.beach_brown, self._select_coordinates(), 'add shark', 'green'))
        self.tiles.append(Tile(self.beach_brown, self._select_coordinates(), 'add boat', 'green'))
        for i in range(3):
            self.tiles.append(Tile(self.beach_brown, self._select_coordinates(), 'dolphin ride', 'red'))
        for i in range(2):
            self.tiles.append(Tile(self.beach_brown, self._select_coordinates(), 'favorable winds', 'red'))
        self.tiles.append(Tile(self.beach_brown, self._select_coordinates(), 'move whale', 'red'))
        self.tiles.append(Tile(self.beach_brown, self._select_coordinates(), 'move shark', 'red'))
        self.tiles.append(Tile(self.beach_brown, self._select_coordinates(), 'move serpent', 'red'))
        self.tiles.append(Tile(self.beach_brown, self._select_coordinates(), 'remove shark', 'red'))
        for i in range(3):
            self.tiles.append(Tile(self.forest_green, self._select_coordinates(), 'add boat', 'green'))
        for i in range(2):
            self.tiles.append(Tile(self.forest_green, self._select_coordinates(), 'add whale', 'green'))
        for i in range(2):
            self.tiles.append(Tile(self.forest_green, self._select_coordinates(), 'add shark', 'green'))
        for i in range(2):
            self.tiles.append(Tile(self.forest_green, self._select_coordinates(), 'whirlpool', 'green'))
        for i in range(2):
            self.tiles.append(Tile(self.forest_green, self._select_coordinates(), 'remove whale', 'red'))
        self.tiles.append(Tile(self.forest_green, self._select_coordinates(), 'remove shark', 'red'))
        self.tiles.append(Tile(self.forest_green, self._select_coordinates(), 'move whale', 'red'))
        self.tiles.append(Tile(self.forest_green, self._select_coordinates(), 'move shark', 'red'))
        self.tiles.append(Tile(self.forest_green, self._select_coordinates(), 'move serpent', 'red'))
        self.tiles.append(Tile(self.forest_green, self._select_coordinates(), 'dolphin ride', 'red'))
        for i in range(4):
            self.tiles.append(Tile(self.rocky_gray, self._select_coordinates(), 'whirlpool', 'green'))
        self.tiles.append(Tile(self.rocky_gray, self._select_coordinates(), 'add shark', 'green'))
        self.tiles.append(Tile(self.rocky_gray, self._select_coordinates(), 'volcano', 'green'))
        self.tiles.append(Tile(self.rocky_gray, self._select_coordinates(), 'remove whale', 'red'))
        self.tiles.append(Tile(self.rocky_gray, self._select_coordinates(), 'remove shark', 'red'))


    def show(self):
        for t in self.tiles:
            t.show()

deck = Deck()
deck.show()
print(len(deck.coordinates))

