# Game Screen Settings
SCREEN_WIDTH = 600  # Width of the game window
SCREEN_HEIGHT = 600  # Height of the game window

# Grid Settings
GRID_SIZE = 3  # Number of rows and columns in the Tic-Tac-Toe grid
CELL_SIZE = SCREEN_WIDTH // GRID_SIZE  # Size of each cell in the grid

# Colors (RGB Format)
LINE_COLOR = (0, 0, 0)  # Color of grid lines (Black)
BACKGROUND_COLOR = (255, 255, 255)  # Background color of the game screen (White)
X_COLOR = (200, 50, 50)  # Color for Player X's symbol (Red)
O_COLOR = (50, 50, 200)  # Color for Player O's symbol (Blue)

# Font Settings
FONT_PATH = "assets/font.ttf"  # Path to the font file used for text rendering

# Sound Effects
MOVE_SOUND_PATH = "assets/move_sound.wav"  # Sound effect for making a move
CLICK_SOUND_PATH = "assets/click_sound.wav"  # Sound effect for button clicks
WIN_SOUND_PATH = "assets/win_sound.wav"  # Sound effect for when a player wins

# Animation Settings
ANIMATION_DURATION = 200  # Duration of animations in milliseconds
