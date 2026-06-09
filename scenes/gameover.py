import pygame
import sys
import os
from typing import Optional

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), "ui"))

from scene import Scene
from label import Button, Label
from core.constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    COLOR_BACKGROUND,
    COLOR_TEXT,
    COLOR_BUTTON_HOVER,
    FONT_KENNEY_SQUARE,
)
from core.scores import HighScores


class GameOverScene(Scene):

    def __init__(self, final_score: int):

        super().__init__()
        self.final_score = final_score
        self.high_scores = HighScores()
        self.is_new_high_score = self.high_scores.update(final_score)
        self._setup_ui()

    def _setup_ui(self) -> None:

        title_font = pygame.font.Font(FONT_KENNEY_SQUARE, 56)
        score_font = pygame.font.Font(FONT_KENNEY_SQUARE, 36)
        button_font = pygame.font.Font(FONT_KENNEY_SQUARE, 32)

        title_text = "GAME OVER!"
        if self.is_new_high_score:
            title_text = "NEW HIGH SCORE!"

        title_width = title_font.size(title_text)[0]
        self.title = Label(
            title_font,
            title_text,
            COLOR_TEXT,
            SCREEN_WIDTH // 2 - title_width // 2,
            100,
        )

        score_text = f"SCORE: {self.final_score}"
        score_width = score_font.size(score_text)[0]
        self.score_label = Label(
            score_font,
            score_text,
            COLOR_TEXT,
            SCREEN_WIDTH // 2 - score_width // 2,
            230,
        )

        high_score_text = f"HIGH SCORE: {self.high_scores.get()}"
        high_score_width = score_font.size(high_score_text)[0]
        self.high_score_label = Label(
            score_font,
            high_score_text,
            COLOR_TEXT,
            SCREEN_WIDTH // 2 - high_score_width // 2,
            310,
        )

        button_width = 200
        button_height = 60
        button_x = SCREEN_WIDTH // 2 - button_width // 2

        self.replay_button = Button(
            button_x,
            450,
            button_width,
            button_height,
            "REPLAY",
            button_font,
            (100, 100, 100),
            COLOR_BUTTON_HOVER,
        )

        self.menu_button = Button(
            button_x,
            540,
            button_width,
            button_height,
            "MENU",
            button_font,
            (100, 100, 100),
            COLOR_BUTTON_HOVER,
        )

    def handle_event(self, event: pygame.event.EventType) -> Optional[str]:

        if event.type == pygame.MOUSEMOTION:
            self.replay_button.update(event.pos)
            self.menu_button.update(event.pos)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.replay_button.rect.collidepoint(event.pos):
                return "gameplay"
            elif self.menu_button.rect.collidepoint(event.pos):
                return "menu"

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                return "gameplay"
            elif event.key == pygame.K_ESCAPE:
                return "menu"

        return None

    def update(self) -> None:

        pass

    def draw(self, screen: pygame.Surface) -> None:

        screen.fill(COLOR_BACKGROUND)
        self.title.draw(screen)
        self.score_label.draw(screen)
        self.high_score_label.draw(screen)
        self.replay_button.draw(screen)
        self.menu_button.draw(screen)
