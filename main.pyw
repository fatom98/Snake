import pygame
from snake.constants import *
from snake.piece import Piece
from snake.game import Game

pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()


def main():

    FPS = 10

    run = True
    paused = False
    game = Game(WIN)

    while run:

        clock.tick(FPS + game.score//2)

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

                        game.set_snake_pos("R")
                        game.modify((0, 1))

                elif event.key == pygame.K_LEFT:

                    if current != "R" and current != "L":

                        game.set_snake_pos("L")
                        game.modify((0, -1))

                elif event.key == pygame.K_UP:

                    if current != "U" and current != "D":

                        game.set_snake_pos("U")
                        game.modify((-1, 0))

                elif event.key == pygame.K_DOWN:

                    if current != "U" and current != "D":

                        game.set_snake_pos("D")
                        game.modify((1, 0))

                elif event.key == pygame.K_SPACE:

                    paused = True

                    while paused:

                        font = pygame.font.SysFont("comicsans", 60, True)
                        text = font.render("Paused", True, WHITE)
                        WIN.blit(text, ((WIDTH - text.get_width())//2, (HEIGHT - text.get_height())//2))

                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                    paused = False

                        pygame.display.update()

        game.update()


if __name__ == "__main__":
    main()
