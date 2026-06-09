import pygame
import sys
import os
from typing import Dict

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "scenes"))

from menu import MenuScene
from gameplay import GameplayScene
from pause import PauseScene
from gameover import GameOverScene
from settingsmenu import SettingsMenuScene


class Game:

    def __init__(self, screen: pygame.Surface):

        self.screen = screen
        self.scenes: Dict[str, any] = {}
        self.current_scene_name = "menu"
        self.gameplay_state = None
        self._init_scenes()

    def _init_scenes(self) -> None:

        self.scenes["menu"] = MenuScene()
        self.scenes["settings"] = SettingsMenuScene()

    def _create_gameplay_scene(self) -> None:

        settings_scene = self.scenes["settings"]
        self.scenes["gameplay"] = GameplayScene(settings_scene.settings.difficulty)

    def switch_scene(self, scene_name: str) -> None:

        if scene_name == "gameplay":
            self._create_gameplay_scene()
            self.current_scene_name = scene_name
        elif scene_name == "gameover":
            gameplay_scene = self.scenes["gameplay"]
            self.scenes["gameover"] = GameOverScene(gameplay_scene.score)
            self.current_scene_name = scene_name
        elif scene_name == "pause":
            gameplay_scene = self.scenes["gameplay"]
            self.gameplay_state = gameplay_scene.store_state()
            self.scenes["pause"] = PauseScene(self.gameplay_state)
            self.current_scene_name = scene_name
        elif scene_name == "gameplay_resume":
            if self.gameplay_state and "gameplay" in self.scenes:
                self.scenes["gameplay"].restore_state(self.gameplay_state)
            self.current_scene_name = "gameplay"
        elif scene_name in self.scenes:
            self.current_scene_name = scene_name
        else:
            self.current_scene_name = scene_name

    def get_current_scene(self):

        return self.scenes.get(self.current_scene_name)

    def handle_event(self, event: pygame.event.EventType) -> None:

        scene = self.get_current_scene()
        if scene:
            next_scene = scene.handle_event(event)
            if next_scene:
                self.switch_scene(next_scene)

    def update(self) -> None:

        scene = self.get_current_scene()
        if scene:
            result = scene.update()
            if result and isinstance(result, str):
                self.switch_scene(result)

    def draw(self) -> None:

        scene = self.get_current_scene()
        if scene:
            scene.draw(self.screen)
