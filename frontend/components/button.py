import pygame

class Button:
    def __init__(self, x, y, width, height, image_path, action):
        self.image = pygame.image.load(image_path)
        self.rect = pygame.Rect(x, y, width, height)
        self.action = action

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.action()
