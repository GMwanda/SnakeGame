import pygame
from pygame.math import Vector2

pygame.init()

cell_size = 25
offset = 75


class snake_class():
    def __init__(self):
        self.body = [Vector2(6, 9), Vector2(5, 9), Vector2(4, 9)]
        self.direction = Vector2(1, 0)
        self.add_segment = False
        self.eat_sound = pygame.mixer.Sound('Assets/eat.mp3')
        self.wall_hit_sound = pygame.mixer.Sound('Assets/wall.mp3')

    def draw(self, screen, snake_color):
        for segment in self.body:
            segment_rect = (offset + segment.x * cell_size, offset + segment.y * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, snake_color, segment_rect, 0, 8)

    def update_self(self):
        self.body.insert(0, self.body[0] + self.direction)
        if self.add_segment == True:
            self.add_segment = False
        else:
            self.body = self.body[:-1]

    def reset(self):
        self.body = [Vector2(6, 9), Vector2(5, 9), Vector2(4, 9)]
        self.direction = Vector2(1, 0)
