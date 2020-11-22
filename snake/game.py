import pygame
from .constants import *
from .board import Board


class Game:

    def __init__(self, win):
        self.win = win
        self.board = Board(self.win)

    def update(self):
        pygame.display.update()
