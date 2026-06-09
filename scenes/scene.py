import pygame
from abc import ABC, abstractmethod
from typing import Optional


class Scene(ABC):

    def __init__(self):

        pass

    @abstractmethod
    def handle_event(self, event: pygame.event.EventType) -> Optional[str]:

        pass

    @abstractmethod
    def update(self) -> None:

        pass

    @abstractmethod
    def draw(self, screen: pygame.Surface) -> None:

        pass
