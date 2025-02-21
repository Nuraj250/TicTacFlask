import pygame
import time
from frontend.settings import CELL_SIZE, GRID_SIZE, LINE_COLOR, MOVE_SOUND_PATH, WIN_SOUND_PATH
from frontend.components.button import Button

class Board:
    def __init__(self, restart_callback):
        self.grid = [["" for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.move_sound = pygame.mixer.Sound(MOVE_SOUND_PATH)
        self.win_sound = pygame.mixer.Sound(WIN_SOUND_PATH)
        self.winning_cells = []
        self.restart_button = Button(200, 500, 200, 50, "assets/restart_button.png", restart_callback)

    def draw(self, screen):
        for row in range(1, GRID_SIZE):
            pygame.draw.line(screen, LINE_COLOR, (0, row * CELL_SIZE), (GRID_SIZE * CELL_SIZE, row * CELL_SIZE), 3)
            pygame.draw.line(screen, LINE_COLOR, (row * CELL_SIZE, 0), (row * CELL_SIZE, GRID_SIZE * CELL_SIZE), 3)

        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                if self.grid[row][col] == "X":
                    pygame.draw.line(screen, (200, 50, 50), 
                                    (col * CELL_SIZE + 20, row * CELL_SIZE + 20), 
                                    ((col + 1) * CELL_SIZE - 20, (row + 1) * CELL_SIZE - 20), 5)
                    pygame.draw.line(screen, (200, 50, 50), 
                                    ((col + 1) * CELL_SIZE - 20, row * CELL_SIZE + 20), 
                                    (col * CELL_SIZE + 20, (row + 1) * CELL_SIZE - 20), 5)
                elif self.grid[row][col] == "O":
                    pygame.draw.circle(screen, (50, 50, 200), 
                                      (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2), 
                                      CELL_SIZE // 3, 5)

    def animate_winner(self, screen):
        for _ in range(5):
            for cell in self.winning_cells:
                row, col = cell
                pygame.draw.rect(screen, (255, 255, 0), 
                                 (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.display.flip()
            time.sleep(0.2)

            for cell in self.winning_cells:
                row, col = cell
                pygame.draw.rect(screen, (255, 255, 255), 
                                 (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.display.flip()
            time.sleep(0.2)

        self.win_sound.play()
        self.restart_button.draw(screen)

    def handle_event(self, event):
        self.restart_button.handle_event(event)
