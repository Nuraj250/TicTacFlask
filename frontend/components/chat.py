import pygame
from frontend.settings import FONT_PATH

class Chat:
    def __init__(self):
        """
        Initializes the in-game chat system.

        - Stores a list of messages.
        - Loads a font from the specified font path.
        - Limits the number of messages displayed to keep the UI clean.
        """
        self.messages = []  # List to store chat messages
        self.font = pygame.font.Font(FONT_PATH, 18)  # Load the font for chat text

    def add_message(self, message):
        """
        Adds a new message to the chat.

        - If the message list exceeds 5, removes the oldest message to maintain a clean display.
        - Appends the new message to the list.

        Parameters:
        - message (str): The text message to add to the chat.
        """
        if len(self.messages) > 5:  # Keep only the last 5 messages
            self.messages.pop(0)  # Remove the oldest message
        self.messages.append(message)  # Add the new message

    def draw(self, screen):
        """
        Renders the chat messages on the game screen.

        - Displays messages from the chat list in a vertical stack.
        - Each message appears slightly lower than the previous one.

        Parameters:
        - screen (pygame.Surface): The game window where the chat is drawn.
        """
        y_offset = 500  # Starting y-coordinate for the chat display
        for msg in self.messages:
            text_surface = self.font.render(msg, True, (50, 50, 50))  # Render text with a dark gray color
            screen.blit(text_surface, (10, y_offset))  # Draw the message at the specified position
            y_offset += 20  # Move down for the next message
