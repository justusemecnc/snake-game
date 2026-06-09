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


class MenuScene(Scene):

    def __init__(self):

        super().__init__()
        self.high_scores = HighScores()
        self._setup_ui()

    def _setup_ui(self) -> None:

        large_font = pygame.font.Font(FONT_KENNEY_SQUARE, 64)
        button_font = pygame.font.Font(FONT_KENNEY_SQUARE, 32)
        small_font = pygame.font.Font(FONT_KENNEY_SQUARE, 24)
        self.high_score_font = small_font

        title_surface = large_font.render("SNAKE", True, COLOR_TEXT)
        title_x = (SCREEN_WIDTH - title_surface.get_width()) // 2
        self.title = Label(large_font, "SNAKE", COLOR_TEXT, title_x, 50)

        button_width = 200
        button_height = 60
        button_x = SCREEN_WIDTH // 2 - button_width // 2

        self.play_button = Button(
            button_x,
            250,
            button_width,
            button_height,
            "PLAY",
            button_font,
            (100, 100, 100),
            COLOR_BUTTON_HOVER,
        )

        self.settings_button = Button(
            button_x,
            330,
            button_width,
            button_height,
            "SETTINGS",
            button_font,
            (100, 100, 100),
            COLOR_BUTTON_HOVER,
        )

        self.exit_button = Button(
            button_x,
            410,
            button_width,
            button_height,
            "EXIT",
            button_font,
            (100, 100, 100),
            COLOR_BUTTON_HOVER,
        )

        self.high_score_label = Label(
            self.high_score_font,
            "HIGH SCORE: 0",
            COLOR_TEXT,
            SCREEN_WIDTH // 2,
            SCREEN_HEIGHT - 100,
        )
        self._refresh_high_score_label()

    def _refresh_high_score_label(self) -> None:

        self.high_scores.load()
        high_score_text = f"HIGH SCORE: {self.high_scores.get()}"
        high_score_width = self.high_score_font.size(high_score_text)[0]
        self.high_score_label.set_text(high_score_text)
        self.high_score_label.set_position(
            SCREEN_WIDTH // 2 - high_score_width // 2,
            SCREEN_HEIGHT - 100,
        )

    def handle_event(self, event: pygame.event.EventType) -> Optional[str]:

        if event.type == pygame.MOUSEMOTION:
            self.play_button.update(event.pos)
            self.settings_button.update(event.pos)
            self.exit_button.update(event.pos)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.play_button.rect.collidepoint(event.pos):
                return "gameplay"
            elif self.settings_button.rect.collidepoint(event.pos):
                return "settings"
            elif self.exit_button.rect.collidepoint(event.pos):
                pygame.quit()
                exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

        return None

    def update(self) -> None:

        self._refresh_high_score_label()

    def draw(self, screen: pygame.Surface) -> None:

        screen.fill(COLOR_BACKGROUND)
        self.title.draw(screen)
        self.play_button.draw(screen)
        self.settings_button.draw(screen)
        self.exit_button.draw(screen)
        self.high_score_label.draw(screen)
