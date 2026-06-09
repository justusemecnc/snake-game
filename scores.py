import json
import os
from constants import SCORES_FILE, DATA_DIR


class HighScores:

    def __init__(self):

        self.high_score = 0
        self.load()

    def load(self) -> None:

        os.makedirs(DATA_DIR, exist_ok=True)

        if os.path.exists(SCORES_FILE):
            try:
                with open(SCORES_FILE, "r") as f:
                    data = json.load(f)
                    self.high_score = data.get("high_score", 0)
            except (json.JSONDecodeError, IOError):
                self._create_defaults()
        else:
            self._create_defaults()

    def save(self) -> None:

        os.makedirs(DATA_DIR, exist_ok=True)

        data = {"high_score": self.high_score}
        with open(SCORES_FILE, "w") as f:
            json.dump(data, f, indent=2)

    def _create_defaults(self) -> None:

        self.high_score = 0
        self.save()

    def update(self, score: int) -> bool:

        if score > self.high_score:
            self.high_score = score
            self.save()
            return True
        return False

    def get(self) -> int:

        return self.high_score
