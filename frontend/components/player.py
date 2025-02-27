import pygame
from frontend.settings import FONT_PATH, CLICK_SOUND_PATH

class Player:
    def __init__(self, name, symbol):
        """
        Initializes a player with a name and a game symbol ('X' or 'O').

        - Stores player details.
        - Loads a font for displaying the player's name and symbol.
        - Loads a click sound to be played when the player makes a move.

        Parameters:
        - name (str): The player's name.
        - symbol (str): The player's symbol ('X' or 'O').

        Attributes:
        - font (pygame.Font): Font used to display player information.
        - click_sound (pygame.mixer.Sound): Sound effect for player actions.
        """
        self.name = name  # Store player name
        self.symbol = symbol  # Store player symbol ('X' or 'O')
        self.font = pygame.font.Font(FONT_PATH, 24)  # Load font for text display
        self.click_sound = pygame.mixer.Sound(CLICK_SOUND_PATH)  # Load click sound effect

    def draw(self, screen, position):
        """
        Renders the player's name and symbol on the screen.

        - Displays the player's name alongside their symbol.

        Parameters:
        - screen (pygame.Surface): The game window where player info is drawn.
        - position (tuple): The (x, y) coordinates where text should be displayed.
        """
        text_surface = self.font.render(f"{self.name}: {self.symbol}", True, (0, 0, 0))  # Render text in black
        screen.blit(text_surface, position)  # Draw text at the specified position

    def play_click_sound(self):
        """
        Plays the click sound when the player makes a move.
        """
        self.click_sound.play()  # Play the stored click sound effect
