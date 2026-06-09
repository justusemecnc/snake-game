import json
import os
from constants import SETTINGS_FILE, DATA_DIR


class Settings:

    def __init__(self):

        self.difficulty = "medium"
        self.load()

    def load(self) -> None:

        os.makedirs(DATA_DIR, exist_ok=True)

        if os.path.exists(SETTINGS_FILE):
            try:
                with open(SETTINGS_FILE, "r") as f:
                    data = json.load(f)
                    self.difficulty = data.get("difficulty", "medium")
            except (json.JSONDecodeError, IOError):
                self._create_defaults()
        else:
            self._create_defaults()

    def save(self) -> None:

        os.makedirs(DATA_DIR, exist_ok=True)

        data = {"difficulty": self.difficulty}
        with open(SETTINGS_FILE, "w") as f:
            json.dump(data, f, indent=2)

    def _create_defaults(self) -> None:

        self.difficulty = "medium"
        self.save()

    def set_difficulty(self, difficulty: str) -> None:

        if difficulty in ("easy", "medium", "hard"):
            self.difficulty = difficulty
            self.save()
