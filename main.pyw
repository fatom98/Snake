import pygame
from snake.constants import *
from snake.piece import Piece
from snake.game import Game

pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
FPS = 10


def main():

    run = True
    game = Game(WIN)

    while run:

        clock.tick(FPS + game.score//3)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if finish := game.finished:

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        run = False
                    elif event.key == pygame.K_a:
                        game.res()

            if event.type == pygame.KEYDOWN:

                current = game.get_snake_pos()

                if event.key == pygame.K_RIGHT:

                    if current != "R" and current != "L":

                        game.modify((0, 1))
                        game.set_snake_pos("R")

                elif event.key == pygame.K_LEFT:

                    if current != "R" and current != "L":
                        game.modify((0, -1))
                        game.set_snake_pos("L")

                elif event.key == pygame.K_UP:

                    if current != "U" and current != "D":
                        game.modify((-1, 0))
                        game.set_snake_pos("U")

                elif event.key == pygame.K_DOWN:

                    if current != "U" and current != "D":
                        game.modify((1, 0))
                        game.set_snake_pos("D")

        game.update()


if __name__ == "__main__":
    main()
