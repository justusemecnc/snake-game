import pygame
import sys
import os
from typing import Optional

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), "ui"))

from scene import Scene
from label import Button, Label
from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    COLOR_BACKGROUND,
    COLOR_TEXT,
    COLOR_BUTTON_HOVER,
    FONT_KENNEY_SQUARE,
)

import importlib

_settings_module = importlib.import_module("settings")
Settings = _settings_module.Settings


class SettingsMenuScene(Scene):

    def __init__(self):

        super().__init__()
        self.settings = Settings()
        self.selected_difficulty = self.settings.difficulty
        self._setup_ui()

    def _setup_ui(self) -> None:

        title_font = pygame.font.Font(FONT_KENNEY_SQUARE, 48)
        label_font = pygame.font.Font(FONT_KENNEY_SQUARE, 28)
        button_font = pygame.font.Font(FONT_KENNEY_SQUARE, 24)

        title_text = "SETTINGS"
        title_width = title_font.size(title_text)[0]
        self.title = Label(
            title_font, title_text, COLOR_TEXT, SCREEN_WIDTH // 2 - title_width // 2, 80
        )

        difficulty_text = "DIFFICULTY:"
        difficulty_width = label_font.size(difficulty_text)[0]
        difficulty_label_x = SCREEN_WIDTH // 2 - difficulty_width // 2
        self.difficulty_label = Label(
            label_font, difficulty_text, COLOR_TEXT, difficulty_label_x, 180
        )

        button_height = 50
        button_y = 240
        button_gap = 16
        button_width = 120
        medium_button_width = 150
        total_width = (
            button_width + button_gap + medium_button_width + button_gap + button_width
        )
        button_group_x = SCREEN_WIDTH // 2 - total_width // 2

        self.easy_button = Button(
            button_group_x,
            button_y,
            button_width,
            button_height,
            "EASY",
            button_font,
            (100, 100, 100),
            COLOR_BUTTON_HOVER,
            on_click=lambda: self._set_difficulty("easy"),
        )

        self.medium_button = Button(
            button_group_x + button_width + button_gap,
            button_y,
            medium_button_width,
            button_height,
            "MEDIUM",
            button_font,
            (100, 100, 100),
            COLOR_BUTTON_HOVER,
            on_click=lambda: self._set_difficulty("medium"),
        )

        self.hard_button = Button(
            button_group_x
            + button_width
            + button_gap
            + medium_button_width
            + button_gap,
            button_y,
            button_width,
            button_height,
            "HARD",
            button_font,
            (100, 100, 100),
            COLOR_BUTTON_HOVER,
            on_click=lambda: self._set_difficulty("hard"),
        )

        self.back_button = Button(
            SCREEN_WIDTH // 2 - 80,
            500,
            160,
            50,
            "BACK",
            button_font,
            (100, 100, 100),
            COLOR_BUTTON_HOVER,
        )

        self._update_difficulty_display()

    def _set_difficulty(self, difficulty: str) -> None:

        self.selected_difficulty = difficulty
        self.settings.set_difficulty(difficulty)
        self._update_difficulty_display()

    def _update_difficulty_display(self) -> None:

        difficulties = [
            (self.easy_button, "easy"),
            (self.medium_button, "medium"),
            (self.hard_button, "hard"),
        ]

        for button, difficulty in difficulties:
            if difficulty == self.selected_difficulty:
                button.color = (100, 200, 100)
                button.current_color = (100, 200, 100)
            else:
                button.color = (100, 100, 100)
                button.current_color = (100, 100, 100)

    def handle_event(self, event: pygame.event.EventType) -> Optional[str]:

        if event.type == pygame.MOUSEMOTION:
            self.easy_button.update(event.pos)
            self.medium_button.update(event.pos)
            self.hard_button.update(event.pos)
            self.back_button.update(event.pos)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.easy_button.handle_click(event.pos)
            self.medium_button.handle_click(event.pos)
            self.hard_button.handle_click(event.pos)

            if self.back_button.rect.collidepoint(event.pos):
                return "menu"

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return "menu"

        return None

    def update(self) -> None:

        pass

    def draw(self, screen: pygame.Surface) -> None:

        screen.fill(COLOR_BACKGROUND)
        self.title.draw(screen)
        self.difficulty_label.draw(screen)
        self.easy_button.draw(screen)
        self.medium_button.draw(screen)
        self.hard_button.draw(screen)
        self.back_button.draw(screen)
