import pygame
from .constants import *


class Piece:

    def __init__(self, win, x, y):
        self.win = win
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.circle(self.win, RED, (self.x, self.y), 5)
