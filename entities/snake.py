import pygame
from typing import List, Tuple
from core.constants import (
    GRID_SIZE,
    COLOR_SNAKE_HEAD,
    COLOR_SNAKE_BODY,
    PLAYFIELD_GRID_WIDTH,
    PLAYFIELD_GRID_HEIGHT,
    PLAYFIELD_OFFSET_X,
    PLAYFIELD_OFFSET_Y,
)


class Snake:

    def __init__(self, start_x: int, start_y: int):

        self.body: List[Tuple[int, int]] = [(start_x, start_y)]
        self.direction = (1, 0)
        self.next_direction = (1, 0)
        self.grow_pending = False

    def set_direction(self, dx: int, dy: int) -> None:

        if (dx, dy) == (-self.direction[0], -self.direction[1]):
            return
        self.next_direction = (dx, dy)

    def update(self) -> None:

        self.direction = self.next_direction
        head_x, head_y = self.body[0]
        dx, dy = self.direction

        new_x = (head_x + dx) % PLAYFIELD_GRID_WIDTH
        new_y = (head_y + dy) % PLAYFIELD_GRID_HEIGHT

        new_head = (new_x, new_y)
        self.body.insert(0, new_head)

        if not self.grow_pending:
            self.body.pop()
        else:
            self.grow_pending = False

    def grow(self) -> None:

        self.grow_pending = True

    def get_head(self) -> Tuple[int, int]:

        return self.body[0]

    def check_wall_collision(self) -> bool:

        return False

    def check_self_collision(self) -> bool:

        head = self.get_head()
        return head in self.body[1:]

    def draw(self, screen: pygame.Surface) -> None:

        for i, (x, y) in enumerate(self.body):
            color = COLOR_SNAKE_HEAD if i == 0 else COLOR_SNAKE_BODY
            rect = pygame.Rect(
                PLAYFIELD_OFFSET_X + x * GRID_SIZE,
                PLAYFIELD_OFFSET_Y + y * GRID_SIZE,
                GRID_SIZE,
                GRID_SIZE,
            )
            pygame.draw.rect(screen, color, rect)
