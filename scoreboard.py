import pygame
from constants import *

class Scoreboard:
    def __init__(self):
        self.score = 0
        self.font = pygame.font.Font(None, 36)

    def increment(self):
        self.score += 1

    def draw(self, screen):
        score_text = self.font.render(f"Score: {self.score}", True, "white")
        screen.blit(score_text, (SCREEN_WIDTH - 150, 10))