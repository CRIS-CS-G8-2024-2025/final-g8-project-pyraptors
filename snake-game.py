import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
YELLOW = (255, 255, 0)

# Clock and speed
clock = pygame.time.Clock()
speed = 10  # Frames per second

# Font for score
font = pygame.font.SysFont(None, 36)

# Snake class
class Snake:
    def __init__(self):
        self.segments = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = (CELL_SIZE, 0)  # start moving right

    def move(self):
        head_x, head_y = self.segments[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)
        self.segments.insert(0, new_head)
        self.segments.pop()  # remove tail unless eating

    def grow(self):
        # When growing, just don't pop tail on next move
        pass

    def change_direction(self, new_dir):
        # Prevent snake from reversing
        opposite = (-self.direction[0], -self.direction[1])
        if new_dir != opposite:
            self.direction = new_dir

    def collided_with_self(self):
        head = self.segments[0]
        return head in self.segments[1:]

    def draw(self, surface):
        for segment in self.segments:
            rect = pygame.Rect(segment[0], segment[1], CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(surface, GREEN, rect)

# Coin class
class Coin:
    def __init__(self):
        self.position = self.random_position()

    def random_position(self):
        x = random.randrange(0, WIDTH, CELL_SIZE)
        y = random.randrange(0, HEIGHT, CELL_SIZE)
        return (x, y)

    def respawn(self, snake_segments):
        while True:
            pos = self.random_position()
            if pos not in snake_segments:
                self.position = pos
                break

    def draw(self, surface):
        center = (self.position[0] + CELL_SIZE // 2, self.position[1] + CELL_SIZE // 2)
        pygame.draw.circle(surface, YELLOW, center, CELL_SIZE // 2)

# Draw score
def draw_score(surface, score):
    text = font.render(f"Score: {score}", True, WHITE)
    surface.blit(text, (10, 10))

def game_over(surface, score):
    surface.fill(BLACK)
    game_over_text = font.render("Game Over!", True, RED)
    score_text = font.render(f"Final Score: {score}", True, WHITE)
    surface.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 3))
    surface.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2))
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()

def main():
    snake = Snake()
    coin = Coin()
    score = 0
    growing = False

    running = True
    while running:
        clock.tick(speed)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Handle key presses to change direction
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction((0, -CELL_SIZE))
                elif event.key == pygame.K_DOWN:
                    snake.change_direction((0, CELL_SIZE))
                elif event.key == pygame.K_LEFT:
                    snake.change_direction((-CELL_SIZE, 0))
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction((CELL_SIZE, 0))

        # Move snake
        head_x, head_y = snake.segments[0]
        dx, dy = snake.direction
        new_head = (head_x + dx, head_y + dy)

        # Check for collisions with walls
        if not (0 <= new_head[0] < WIDTH and 0 <= new_head[1] < HEIGHT):
            game_over(screen, score)

        # Check for collisions with self
        if new_head in snake.segments:
            game_over(screen, score)

        # Insert new head
        snake.segments.insert(0, new_head)

        # Check if coin eaten
        if new_head == coin.position:
            score += 1
            # Don't remove tail segment -> grow snake
            coin.respawn(snake.segments)
        else:
            # Normal movement - remove tail
            snake.segments.pop()

        # Draw everything
        screen.fill(BLACK)
        snake.draw(screen)
        coin.draw(screen)
        draw_score(screen, score)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()