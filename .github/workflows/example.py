import pygame
import random

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 600, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Snake properties
BLOCK_SIZE = 20
snake_speed = 10

# Snake starting position and direction
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
direction = "RIGHT"

# Food position
food_pos = [random.randrange(1, (WIDTH // BLOCK_SIZE)) * BLOCK_SIZE, 
            random.randrange(1, (HEIGHT // BLOCK_SIZE)) * BLOCK_SIZE]

# Score
score = 0

# Update snake position
def update_snake(direction, snake_body):
    if direction == "RIGHT":
        snake_pos[0] += BLOCK_SIZE
    elif direction == "LEFT":
        snake_pos[0] -= BLOCK_SIZE
    elif direction == "UP":
        snake_pos[1] -= BLOCK_SIZE
    elif direction == "DOWN":
        snake_pos[1] += BLOCK_SIZE
    snake_body.insert(0, list(snake_pos))

# Check if the snake has collided with itself or the walls
def check_collision(snake_body):
    if snake_pos[0] >= WIDTH or snake_pos[0] < 0 or snake_pos[1] >= HEIGHT or snake_pos[1] < 0:
        return True
    for block in snake_body[1:]:
        if snake_pos == block:
            return True
    return False

# Main game loop
def game_loop():
    global direction, snake_pos, snake_body, food_pos, score
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    direction = "RIGHT"
                elif event.key == pygame.K_LEFT:
                    direction = "LEFT"
                elif event.key == pygame.K_UP:
                    direction = "UP"
                elif event.key == pygame.K_DOWN:
                    direction = "DOWN"

        update_snake(direction, snake_body)
        
        if snake_pos == food_pos:
            food_pos = [random.randrange(1, (WIDTH // BLOCK_SIZE)) * BLOCK_SIZE, 
                        random.randrange(1, (HEIGHT // BLOCK_SIZE)) * BLOCK_SIZE]
            score += 1
        else:
            snake_body.pop()
        
        WIN.fill(WHITE)
        for block in snake_body:
            pygame.draw.rect(WIN, GREEN, pygame.Rect(block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(WIN, RED, pygame.Rect(food_pos[0], food_pos[1], BLOCK_SIZE, BLOCK_SIZE))
        
        if check_collision(snake_body):
            pygame.quit()
            quit()
        
        pygame.display.flip()
        pygame.time.Clock().tick(snake_speed)

game_loop()
