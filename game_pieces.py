import pygame



# def create_game_pieces(image):
#     game_pieces = pygame.image.load(image).convert_alpha()
#     game_pieces = pygame.transform.scale(game_pieces, (100, 50))
#     red_piece = game_pieces.subsurface(0, 0, 20, 50)
#     return red_piece

# create_game_pieces('game_pieces.png')


class GamePiece:
    def __init__(self, color, value):
        self.color = color
        self.value = value
        self.swimming = False
        self.boat = False
        self.safe = False
        # self.rect = create_game_pieces('game_pieces.png')


    # def load_image(self):
    #     image = pygame.image.load('.png').convert_alpha()
    #     image = pygame.transform.scale(image, (50, 50))
    #     return image

    def draw(self, surface, coords):
        self.rect.x = coords[0]
        self.rect.y = coords[1]
        return surface.blit(self.image, coords)

# red_piece = GamePiece('red', 6)
# print(red_piece.rect)