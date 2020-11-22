import pygame
from .constants import *
from pprint import pprint


class Board:

    def __init__(self, win):
        self.win = win
        self.board = []
        self.create_board()

    def create_board(self):

        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                self.board[row].append("")

        self.draw()

    def draw(self):

        for row in range(ROWS + 1):
            pygame.draw.line(self.win, WHITE, (row * SQUARE_SIZE, 0), (row * SQUARE_SIZE, HEIGHT), 1)

        for col in range(COLS + 1):
            pygame.draw.line(self.win, WHITE, (0, col * SQUARE_SIZE), (WIDTH, col * SQUARE_SIZE), 1)

        print(self.board)
