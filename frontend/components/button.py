import pygame

class Button:
    def __init__(self, x, y, width, height, image_path, action):
        """
        Initializes the button with position, size, image, and action.

        - Loads the button image from the given path.
        - Sets the button's rectangle dimensions.
        - Stores the action (callback function) to be executed on click.

        Parameters:
        - x (int): X-coordinate of the button.
        - y (int): Y-coordinate of the button.
        - width (int): Width of the button.
        - height (int): Height of the button.
        - image_path (str): File path to the button's image.
        - action (function): Function to execute when the button is clicked.
        """
        self.image = pygame.image.load(image_path)  # Load button image
        self.rect = pygame.Rect(x, y, width, height)  # Define button boundaries
        self.action = action  # Store callback function

    def draw(self, screen):
        """
        Draws the button on the screen.

        - Blits the button image at its defined position.

        Parameters:
        - screen (pygame.Surface): The game window where the button is drawn.
        """
        screen.blit(self.image, self.rect.topleft)

    def handle_event(self, event):
        """
        Handles user interactions with the button.

        - Checks if a mouse click event occurs within the button's boundaries.
        - Calls the stored action if the button is clicked.

        Parameters:
        - event (pygame.Event): The event captured by the game loop.
        """
        if event.type == pygame.MOUSEBUTTONDOWN:  # Detect mouse button press
            if self.rect.collidepoint(event.pos):  # Check if click is inside button
                self.action()  # Execute the assigned action
