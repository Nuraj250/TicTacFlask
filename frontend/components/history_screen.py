import pygame
from frontend.settings import FONT_PATH
from frontend.services.api_client import get_match_history

class HistoryScreen:
    def __init__(self):
        """
        Initializes the match history screen.

        - Loads the font for displaying match history.
        - Fetches past match data from the API.

        Attributes:
        - font (pygame.Font): Font used to render text.
        - matches (list): List of match history data retrieved from the API.
        """
        self.font = pygame.font.Font(FONT_PATH, 24)  # Load the font for displaying history
        self.matches = get_match_history()  # Fetch match history from API

    def draw(self, screen):
        """
        Renders the match history on the game screen.

        - Clears the screen with a white background.
        - Iterates through match history and displays player names and the winner.

        Parameters:
        - screen (pygame.Surface): The game window where history is drawn.
        """
        screen.fill((255, 255, 255))  # Clear screen with white background

        y_offset = 50  # Starting position for displaying match history
        for match in self.matches:
            # Format the match text as "Player1 vs Player2 - Winner: Winner"
            text = f"{match['player1']} vs {match['player2']} - Winner: {match['winner']}"
            text_surface = self.font.render(text, True, (0, 0, 0))  # Render the text in black
            screen.blit(text_surface, (50, y_offset))  # Display text at specified position
            y_offset += 30  # Move down for the next match
