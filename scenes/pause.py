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


class PauseScene(Scene):

    def __init__(self, gameplay_state: dict):

        super().__init__()
        self.gameplay_state = gameplay_state
        self._setup_ui()

    def _setup_ui(self) -> None:

        title_font = pygame.font.Font(FONT_KENNEY_SQUARE, 48)
        button_font = pygame.font.Font(FONT_KENNEY_SQUARE, 32)

        title_surface = title_font.render("PAUSED", True, COLOR_TEXT)
        title_x = SCREEN_WIDTH // 2 - title_surface.get_width() // 2

        self.title = Label(title_font, "PAUSED", COLOR_TEXT, title_x, 150)

        button_width = 200
        button_height = 60
        button_x = SCREEN_WIDTH // 2 - button_width // 2

        self.resume_button = Button(
            button_x,
            300,
            button_width,
            button_height,
            "RESUME",
            button_font,
            (100, 100, 100),
            COLOR_BUTTON_HOVER,
        )

        self.menu_button = Button(
            button_x,
            400,
            button_width,
            button_height,
            "MENU",
            button_font,
            (100, 100, 100),
            COLOR_BUTTON_HOVER,
        )

    def handle_event(self, event: pygame.event.EventType) -> Optional[str]:

        if event.type == pygame.MOUSEMOTION:
            self.resume_button.update(event.pos)
            self.menu_button.update(event.pos)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.resume_button.rect.collidepoint(event.pos):
                return "gameplay_resume"
            elif self.menu_button.rect.collidepoint(event.pos):
                return "menu"

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return "gameplay_resume"

        return None

    def update(self) -> None:

        pass

    def draw(self, screen: pygame.Surface) -> None:

        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(128)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))

        self.title.draw(screen)
        self.resume_button.draw(screen)
        self.menu_button.draw(screen)
