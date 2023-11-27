import pygame
from pygame.math import Vector2

pygame.init()


class food_class():
    def __init__(self):
        self.position = Vector2(5, 6)

    def draw(self, cell_size, screen, food_color):
        food_rect = pygame.Rect(self.position.x * cell_size, self.position.y * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, food_color, food_rect)
