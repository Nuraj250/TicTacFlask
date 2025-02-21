import pygame
from frontend.settings import FONT_PATH, CLICK_SOUND_PATH

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.font = pygame.font.Font(FONT_PATH, 24)
        self.click_sound = pygame.mixer.Sound(CLICK_SOUND_PATH)

    def draw(self, screen, position):
        text_surface = self.font.render(f"{self.name}: {self.symbol}", True, (0, 0, 0))
        screen.blit(text_surface, position)

    def play_click_sound(self):
        self.click_sound.play()
