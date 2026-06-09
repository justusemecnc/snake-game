import pygame
import random
from typing import Tuple
from constants import (
    GRID_SIZE,
    COLOR_FOOD,
    PLAYFIELD_GRID_WIDTH,
    PLAYFIELD_GRID_HEIGHT,
    PLAYFIELD_OFFSET_X,
    PLAYFIELD_OFFSET_Y,
)


class Food:

    def __init__(self, occupied_cells: Tuple[Tuple[int, int], ...]):

        self.position: Tuple[int, int] = (0, 0)
        self.spawn(occupied_cells)

    def spawn(self, occupied_cells: Tuple[Tuple[int, int], ...]) -> None:

        available = [
            (x, y)
            for x in range(PLAYFIELD_GRID_WIDTH)
            for y in range(PLAYFIELD_GRID_HEIGHT)
            if (x, y) not in occupied_cells
        ]

        if available:
            self.position = random.choice(available)

    def get_position(self) -> Tuple[int, int]:

        return self.position

    def draw(self, screen: pygame.Surface) -> None:

        x, y = self.position
        rect = pygame.Rect(
            PLAYFIELD_OFFSET_X + x * GRID_SIZE,
            PLAYFIELD_OFFSET_Y + y * GRID_SIZE,
            GRID_SIZE,
            GRID_SIZE,
        )
        pygame.draw.rect(screen, COLOR_FOOD, rect)
