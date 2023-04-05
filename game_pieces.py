import pygame


def create_game_pieces(color, left):
    game_pieces = pygame.image.load('game_pieces.png').convert_alpha()
    game_pieces = pygame.transform.scale(game_pieces, (100, 50))
    piece_png = game_pieces.subsurface(left, 0, 20, 50)
    title = f'{color}_piece.png'
    pygame.image.save(piece_png, title)


class GamePiece:
    def __init__(self, color, value, png):
        self.color = color
        self.value = value
        self.swimming = False
        self.boat = False
        self.safe = False
        self.png = png
        self.image = self.load_image()
        self.rect = self.image.get_rect()

    def load_image(self):
        image = pygame.image.load(self.png).convert_alpha()
        image = pygame.transform.scale(image, (50, 50))
        return image

    def draw(self, surface, coords):
        self.rect.x = coords[0]
        self.rect.y = coords[1]
        return surface.blit(self.image, coords)

# red_piece = GamePiece('red', 6, 'red_piece.png')
# print(red_piece.rect)