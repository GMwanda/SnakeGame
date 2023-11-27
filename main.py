import pygame
from pygame import Vector2

from GameGrid import game_class

pygame.init()

# KEY VARIABLES
title_font = pygame.font.Font(None, 50)
score_font = pygame.font.Font(None, 30)
cell_size = 25
number_of_cells = 20
offset = 75
WIDTH = 2 * offset + cell_size * number_of_cells
HEIGHT = 2 * offset + cell_size * number_of_cells
fps = 60
timer = pygame.time.Clock()
background_color = (200, 200, 200)
snake_color = (0, 100, 0)  # Green for the snake
food_color = (255, 0, 0)  # Red for the food
obstacle_color = (0, 0, 0)  # Gray for obstacles (if any)

snake_update = pygame.USEREVENT
pygame.time.set_timer(snake_update, 200)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

food_element = pygame.image.load("Assets/food.png")

game = game_class()


def game_loop():
    running = True
    while running:
        screen.fill(background_color)

        for event in pygame.event.get():

            if event.type == snake_update:
                game.update()

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if game.state == "STOPPED":
                    game.state = "RUNNING"
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_UP and game.snake.direction != Vector2(0, 1):
                    game.snake.direction = Vector2(0, -1)
                elif event.key == pygame.K_DOWN and game.snake.direction != Vector2(0, -1):
                    game.snake.direction = Vector2(0, 1)
                elif event.key == pygame.K_RIGHT and game.snake.direction != Vector2(-1, 0):
                    game.snake.direction = Vector2(1, 0)
                elif event.key == pygame.K_LEFT and game.snake.direction != Vector2(1, 0):
                    game.snake.direction = Vector2(-1, 0)

        title_surface = title_font.render("Retro Snake", True, obstacle_color)
        screen.blit(title_surface, (offset - 5, 20))

        score_surface = score_font.render(f'Score: {game.score}', True, obstacle_color)
        screen.blit(score_surface, (offset - 5, offset + cell_size * number_of_cells + 10))

        high_score_surface = score_font.render(f'Highest Score: {game.high_score}', True, obstacle_color)
        screen.blit(high_score_surface, (offset - 5, offset + cell_size * number_of_cells + 40))

        game.draw(screen, cell_size, snake_color, food_element)
        pygame.draw.rect(screen, obstacle_color,
                         (offset - 5, offset - 5, cell_size * number_of_cells + 10, cell_size * number_of_cells + 10),
                         5)

        pygame.display.update()
        timer.tick(fps)
        pygame.display.flip()


game_loop()
