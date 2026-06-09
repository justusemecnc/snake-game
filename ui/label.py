import pygame
from typing import Optional, Callable, Tuple


class Label:

    def __init__(
        self,
        font: pygame.font.Font,
        text: str,
        color: Tuple[int, int, int],
        x: int,
        y: int,
    ):

        self.font = font
        self.text = text
        self.color = color
        self.x = x
        self.y = y
        self.surface = None
        self.rect = None
        self._render()

    def _render(self) -> None:

        self.surface = self.font.render(self.text, True, self.color)
        self.rect = self.surface.get_rect(topleft=(self.x, self.y))

    def set_text(self, text: str) -> None:

        self.text = text
        self._render()

    def set_position(self, x: int, y: int) -> None:

        self.x = x
        self.y = y
        self.rect.topleft = (x, y)

    def draw(self, screen: pygame.Surface) -> None:

        if self.surface and self.rect:
            screen.blit(self.surface, self.rect)


class Panel:

    def __init__(
        self, x: int, y: int, width: int, height: int, color: Tuple[int, int, int]
    ):

        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.children = []

    def add_child(self, child) -> None:

        self.children.append(child)

    def set_position(self, x: int, y: int) -> None:

        self.rect.x = x
        self.rect.y = y

    def draw(self, screen: pygame.Surface) -> None:

        pygame.draw.rect(screen, self.color, self.rect)
        for child in self.children:
            if hasattr(child, "draw"):
                child.draw(screen)


class Button:

    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        text: str,
        font: pygame.font.Font,
        color: Tuple[int, int, int],
        hover_color: Tuple[int, int, int],
        on_click: Optional[Callable] = None,
    ):

        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = font
        self.color = color
        self.hover_color = hover_color
        self.current_color = color
        self.on_click = on_click
        self.is_hovering = False
        self.text_surface = None
        self.text_rect = None
        self._render_text()

    def _render_text(self) -> None:

        self.text_surface = self.font.render(self.text, True, (255, 255, 255))
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)

    def update(self, mouse_pos: Tuple[int, int]) -> None:

        was_hovering = self.is_hovering
        self.is_hovering = self.rect.collidepoint(mouse_pos)

        if self.is_hovering != was_hovering:
            self.current_color = self.hover_color if self.is_hovering else self.color

    def handle_click(self, mouse_pos: Tuple[int, int]) -> None:

        if self.rect.collidepoint(mouse_pos) and self.on_click:
            self.on_click()

    def set_position(self, x: int, y: int) -> None:

        self.rect.x = x
        self.rect.y = y
        self._render_text()

    def draw(self, screen: pygame.Surface) -> None:

        pygame.draw.rect(screen, self.current_color, self.rect, border_radius=4)
        if self.text_surface and self.text_rect:
            screen.blit(self.text_surface, self.text_rect)
