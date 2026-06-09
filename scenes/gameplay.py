import pygame
import sys
import os
from typing import Optional

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), "entities"))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), "ui"))

from scene import Scene
from label import Label
from snake import Snake
from food import Food
from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    COLOR_BACKGROUND,
    COLOR_GRID,
    COLOR_TEXT,
    GRID_SIZE,
    FPS,
    DIFFICULTY_SPEEDS,
    FONT_KENNEY_SQUARE,
    PLAYFIELD_GRID_WIDTH,
    PLAYFIELD_GRID_HEIGHT,
    PLAYFIELD_OFFSET_X,
    PLAYFIELD_OFFSET_Y,
    PLAYFIELD_PIXEL_WIDTH,
    PLAYFIELD_PIXEL_HEIGHT,
)


class GameplayScene(Scene):

    def __init__(self, difficulty: str = "medium"):

        super().__init__()
        self.difficulty = difficulty
        self.speed = DIFFICULTY_SPEEDS.get(difficulty, 6)
        self.tick_counter = 0

        start_x = PLAYFIELD_GRID_WIDTH // 2
        start_y = PLAYFIELD_GRID_HEIGHT // 2
        self.snake = Snake(start_x, start_y)
        self.food = Food(tuple(self.snake.body))
        self.score = 0
        self.paused = False

        self._setup_ui()

    def _setup_ui(self) -> None:

        font = pygame.font.Font(FONT_KENNEY_SQUARE, 28)
        self.score_font = font
        self.score_label = Label(font, f"SCORE: {self.score}", COLOR_TEXT, 0, 18)
        self._update_score_position()

    def _update_score_position(self) -> None:

        text = f"SCORE: {self.score}"
        width = self.score_font.size(text)[0]
        self.score_label.set_position(SCREEN_WIDTH // 2 - width // 2, 18)

    def handle_event(self, event: pygame.event.EventType) -> Optional[str]:

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return "pause"
            elif event.key in (pygame.K_UP, pygame.K_w):
                self.snake.set_direction(0, -1)
            elif event.key in (pygame.K_DOWN, pygame.K_s):
                self.snake.set_direction(0, 1)
            elif event.key in (pygame.K_LEFT, pygame.K_a):
                self.snake.set_direction(-1, 0)
            elif event.key in (pygame.K_RIGHT, pygame.K_d):
                self.snake.set_direction(1, 0)

        return None

    def update(self) -> None:

        self.tick_counter += 1

        if self.tick_counter >= FPS // self.speed:
            self.tick_counter = 0
            self.snake.update()

            if self.snake.check_wall_collision() or self.snake.check_self_collision():
                return "gameover"

            if self.snake.get_head() == self.food.get_position():
                self.snake.grow()
                self.score += 10
                self.score_label.set_text(f"SCORE: {self.score}")
                self._update_score_position()
                self.food.spawn(tuple(self.snake.body))

    def draw(self, screen: pygame.Surface) -> None:

        screen.fill(COLOR_BACKGROUND)
        self._draw_grid(screen)
        self.snake.draw(screen)
        self.food.draw(screen)
        self.score_label.draw(screen)

    def _draw_grid(self, screen: pygame.Surface) -> None:

        for x in range(
            PLAYFIELD_OFFSET_X,
            PLAYFIELD_OFFSET_X + PLAYFIELD_PIXEL_WIDTH + 1,
            GRID_SIZE,
        ):
            pygame.draw.line(
                screen,
                COLOR_GRID,
                (x, PLAYFIELD_OFFSET_Y),
                (x, PLAYFIELD_OFFSET_Y + PLAYFIELD_PIXEL_HEIGHT),
                1,
            )

        for y in range(
            PLAYFIELD_OFFSET_Y,
            PLAYFIELD_OFFSET_Y + PLAYFIELD_PIXEL_HEIGHT + 1,
            GRID_SIZE,
        ):
            pygame.draw.line(
                screen,
                COLOR_GRID,
                (PLAYFIELD_OFFSET_X, y),
                (PLAYFIELD_OFFSET_X + PLAYFIELD_PIXEL_WIDTH, y),
                1,
            )

    def store_state(self) -> dict:

        return {
            "snake_body": self.snake.body.copy(),
            "snake_direction": self.snake.direction,
            "food_position": self.food.position,
            "score": self.score,
        }

    def restore_state(self, state: dict) -> None:

        self.snake.body = state["snake_body"]
        self.snake.direction = state["snake_direction"]
        self.snake.next_direction = state["snake_direction"]
        self.food.position = state["food_position"]
        self.score = state["score"]
        self.score_label.set_text(f"SCORE: {self.score}")
        self._update_score_position()
