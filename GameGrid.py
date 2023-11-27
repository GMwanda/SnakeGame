import pygame

from GameFood import food_class
from SnakeBody import snake_class

pygame.init()

number_of_cells = 20


class game_class():
    def __init__(self):
        self.snake = snake_class()
        self.food = food_class(self.snake.body)
        self.state = "RUNNING"
        self.score = 0
        self.high_score = 0

    def draw(self, screen, cell_size, snake_color, food_element):
        self.food.draw(cell_size, screen, food_element)
        self.snake.draw(screen, snake_color)

    def update(self):
        if self.state == "RUNNING":
            self.snake.update_self()
            self.check_collision_food()
            self.collision_with_tail()
            self.check_collision_with_edges()

    def check_collision_food(self):
        if self.snake.body[0] == self.food.position:
            self.food.position = self.food.generate_random_position(self.snake.body)
            self.snake.add_segment = True
            self.score += 1
            self.snake.eat_sound.play()

    def check_collision_with_edges(self):
        if self.snake.body[0].x == number_of_cells or self.snake.body[0].x == -1:
            self.game_over()
        if self.snake.body[0].y == number_of_cells or self.snake.body[0].y == -1:
            self.game_over()

    def game_over(self):
        self.snake.reset()
        self.food.position = self.food.generate_random_position(self.snake.body)
        self.state = "STOPPED"
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.snake.wall_hit_sound.play()

    def collision_with_tail(self):
        headless_body = self.snake.body[1:]
        if self.snake.body[0] in headless_body:
            self.game_over()
