import random

import pygame
from pygame.math import Vector2

pygame.init()

number_of_cells = 20
offset = 75


class food_class():
    def __init__(self, snake_body):
        self.position = self.generate_random_position(snake_body)

    def draw(self, cell_size, screen, food_element):
        food_rect = pygame.Rect(offset + self.position.x * cell_size, offset + self.position.y * cell_size, cell_size,
                                cell_size)
        screen.blit(food_element, food_rect)

    def generate_random_cell(self):
        x = random.randint(0, number_of_cells - 1)
        y = random.randint(0, number_of_cells - 1)
        return Vector2(x, y)

    def generate_random_position(self, snake_body):
        position = self.generate_random_cell()
        while position in snake_body:
            position = self.generate_random_cell()

        return position
