import pygame

from GameFood import food_class

pygame.init()

# KEY VARIABLES
cell_size = 30
number_of_cells = 25
WIDTH = cell_size * number_of_cells
HEIGHT = cell_size * number_of_cells
fps = 60
timer = pygame.time.Clock()
background_color = (0, 0, 0)  # Black background
snake_color = (0, 255, 0)  # Green for the snake
food_color = (255, 0, 0)  # Red for the food
obstacle_color = (128, 128, 128)  # Gray for obstacles (if any)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

food = food_class()


def game_loop():
    running = True
    while running:
        screen.fill(background_color)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        food.draw(cell_size, screen, food_color)

        pygame.display.update()
        timer.tick(fps)
        pygame.display.flip()


game_loop()
