import pygame
from frontend.settings import FONT_PATH

class Chat:
    def __init__(self):
        self.messages = []
        self.font = pygame.font.Font(FONT_PATH, 18)
    
    def add_message(self, message):
        if len(self.messages) > 5:
            self.messages.pop(0)
        self.messages.append(message)

    def draw(self, screen):
        y_offset = 500
        for msg in self.messages:
            text_surface = self.font.render(msg, True, (50, 50, 50))
            screen.blit(text_surface, (10, y_offset))
            y_offset += 20
