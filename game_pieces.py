import pygame


def create_game_pieces(color, left):
    game_pieces = pygame.image.load('game_pieces.png').convert_alpha()
    game_pieces = pygame.transform.scale(game_pieces, (100, 50))
    piece_png = game_pieces.subsurface(left, 0, 20, 50)
    title = f'{color}_piece.png'
    pygame.image.save(piece_png, title)


class GamePiece:
    def __init__(self, color, value, png, x, y):
        self.color = color
        self.value = value
        self.swimming = False
        self.boat = False
        self.safe = False
        self.alive = True
        self.png = png
        self.image = self.load_image()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def load_image(self):
        image = pygame.image.load(self.png).convert_alpha()
        return image

    def draw(self, surface, coords):
        return surface.blit(self.image, coords)

# red_piece = GamePiece('red', 6, 'red_piece.png')
# print(red_piece.rect)