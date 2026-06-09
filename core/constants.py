import os

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720


COLOR_BACKGROUND = (30, 30, 30)
COLOR_GRID = (50, 50, 50)
COLOR_SNAKE_HEAD = (100, 255, 100)
COLOR_SNAKE_BODY = (80, 200, 80)
COLOR_FOOD = (255, 80, 80)
COLOR_TEXT = (255, 255, 255)
COLOR_TEXT_DIM = (180, 180, 180)
COLOR_BUTTON_HOVER = (80, 200, 200)


GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE


PLAYFIELD_GRID_WIDTH = 56
PLAYFIELD_GRID_HEIGHT = 28
PLAYFIELD_PIXEL_WIDTH = PLAYFIELD_GRID_WIDTH * GRID_SIZE
PLAYFIELD_PIXEL_HEIGHT = PLAYFIELD_GRID_HEIGHT * GRID_SIZE
PLAYFIELD_OFFSET_X = (SCREEN_WIDTH - PLAYFIELD_PIXEL_WIDTH) // 2
PLAYFIELD_OFFSET_Y = (SCREEN_HEIGHT - PLAYFIELD_PIXEL_HEIGHT) // 2

FPS = 60


DIFFICULTY_SPEEDS = {
    "easy": 4,
    "medium": 6,
    "hard": 10,
}


ASSET_DIR = os.path.join(ROOT_DIR, "assets")
FONT_DIR = os.path.join(ASSET_DIR, "fonts")
UI_DIR = os.path.join(ASSET_DIR, "ui")
DATA_DIR = os.path.join(ROOT_DIR, "data")


FONT_KENNEY_SQUARE = os.path.join(FONT_DIR, "Kenney Pixel Square.ttf")
FONT_KENNEY = os.path.join(FONT_DIR, "Kenney Pixel.ttf")


BLOCK_GREEN = os.path.join(UI_DIR, "green.png")
BLOCK_RED = os.path.join(UI_DIR, "red.png")
BLOCK_GREY = os.path.join(UI_DIR, "grey.png")
BLOCK_BLUE = os.path.join(UI_DIR, "blue.png")
BLOCK_YELLOW = os.path.join(UI_DIR, "yellow.png")


SCORES_FILE = os.path.join(DATA_DIR, "scores.json")
SETTINGS_FILE = os.path.join(DATA_DIR, "settings.json")
