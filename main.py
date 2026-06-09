import pygame
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "scenes"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "entities"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "ui"))

from core.constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from core.game import Game


def main() -> None:

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake Game")

    clock = pygame.time.Clock()
    game = Game(screen)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            game.handle_event(event)

        game.update()
        game.draw()
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
