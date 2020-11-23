import pygame
from .constants import *


class Piece:

    def __init__(self, win, row, col):
        self.win = win
        self.row = row
        self.col = col

    def draw(self):
        x = self.col * SQUARE_SIZE + SQUARE_SIZE//2
        y = self.row * SQUARE_SIZE + SQUARE_SIZE//2
        pygame.draw.circle(self.win, RED, (x, y), RADIUS)
