import pygame
import random
import json
from .constants import *
from .snake import Snake
from .piece import Piece


class Game:

    def __init__(self, win):
        self.win = win
        self.font = pygame.font.SysFont(None, 60, True)
        self.font2 = pygame.font.SysFont(None, 40, True)
        self.res()

    def res(self):
        self.pieces = []
        self.finished = False
        self.score = 0

        with open("assets/pref.json", "r") as f:
            data = json.load(f)

        self.high_score = data["high_score"]
        self.snake = Snake(self.win)

    def draw(self):

        for row in range(ROWS):
            pygame.draw.line(self.win, WHITE, (0, row * SQUARE_SIZE), (WIDTH, row * SQUARE_SIZE))

        for col in range(COLS):
            pygame.draw.line(self.win, WHITE, (col * SQUARE_SIZE, 0), (col * SQUARE_SIZE, HEIGHT))

    def update(self):

        if not self.snake.finish:

            self.win.fill(BLACK)

            self.snake.pieces = self.pieces

            if len(self.pieces) < 3:
                row, col = random.randint(0, ROWS - 1), random.randint(0, COLS - 1)
                piece = Piece(self.win, row, col)
                self.pieces.append(piece)

            for piece in self.pieces:
                piece.draw()

            # self.draw()
            self.snake.move()
            self.pieces = self.snake.pieces

        else:
            self.win.fill(WHITE)
            text = self.font.render("You Lost!!! Q or A", True, BLACK)
            self.win.blit(text, ((WIDTH - text.get_width())//2, (HEIGHT - text.get_height())//2))

            obj = {"high_score": self.high_score}

            with open("assets/pref.json", "w") as f:
                json.dump(obj, f, indent=2)

            self.finished = True

        self.score = self.snake.score

        if self.high_score <= self.score:
            self.high_score = self.score

        score = self.font2.render(f"Score: {self.score}", True, BLUE)
        self.win.blit(score, (WIDTH - score.get_width() - 10, score.get_height() - 10))

        high_score = self.font2.render(f"High Score: {self.high_score}", True, BLUE)
        self.win.blit(high_score, (10, score.get_height() - 10))

        pygame.display.update()

    def modify(self, direction: tuple):
        self.snake.direction = direction

    def get_snake_pos(self):
        return self.snake.current

    def set_snake_pos(self, flag):
        self.snake.current = flag
