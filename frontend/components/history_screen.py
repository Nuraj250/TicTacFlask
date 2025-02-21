import pygame
from frontend.settings import FONT_PATH
from frontend.services.api_client import get_match_history

class HistoryScreen:
    def __init__(self):
        self.font = pygame.font.Font(FONT_PATH, 24)
        self.matches = get_match_history()

    def draw(self, screen):
        screen.fill((255, 255, 255))
        y_offset = 50
        for match in self.matches:
            text = f"{match['player1']} vs {match['player2']} - Winner: {match['winner']}"
            text_surface = self.font.render(text, True, (0, 0, 0))
            screen.blit(text_surface, (50, y_offset))
            y_offset += 30
