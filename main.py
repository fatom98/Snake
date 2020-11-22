import pygame
from snake.constants import *
from snake.piece import Piece
from snake.game import Game

pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()


def main():

    run = True
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        game.update()


if __name__ == "__main__":
    main()
