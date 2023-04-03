import pygame

class GamePiece:
    def __init__(self, value):
        self.value = value
        self.swimming = False
        self.boat = False
        self.safe = False