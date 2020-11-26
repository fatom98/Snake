import pygame
import random
from .constants import *


class Snake:

    def __init__(self, win):
        self.win = win
        self.body = [[random.randint(0, ROWS - 1), random.randint(0, COLS - 1)]]
        self.pieces = []
        self.length = 1
        self.direction = (0, 0)
        self.turn = None
        self.current = None
        self.finish = False
        self.score = 0

    def draw(self):

        for row, col in self.body:

            if row != -1 and row != ROWS and col != -1 and col != COLS:
                for piece in self.pieces:

                    if piece.row == row and piece.col == col:
                        self.length += 1
                        self.score += 1
                        self.pieces.remove(piece)

                x1 = col * SQUARE_SIZE
                y1 = row * SQUARE_SIZE
                pygame.draw.rect(self.win, BLACK, (x1, y1, SQUARE_SIZE, SQUARE_SIZE))

            else:
                self.finished()

    def move(self):
        x_pos, y_pos = self.body[-1][0] + self.direction[0], self.body[-1][1] + self.direction[1]

        if [x_pos, y_pos] in self.body and self.direction != (0, 0):
            self.finished()

        else:
            self.body.append([x_pos, y_pos])

        if len(self.body) > self.length:
            del self.body[0]

        self.draw()

    def finished(self):
        self.finish = True
