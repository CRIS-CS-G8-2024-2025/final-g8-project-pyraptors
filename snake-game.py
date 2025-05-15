'''
scroing system
'''
import pygame

# Initialize Pygame's font module
pygame.font.init()

# Set up the font and size for displaying the score
font = pygame.font.SysFont("arial", 30)

# Initialize score
score = 0

def draw_score(screen, score):
    """
    Draws the current score on the screen.
    :param screen: The Pygame screen surface
    :param score: The current score to display
    """
    # Render the score text
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))  # White color
    # Display the score in the top-left corner
    screen.blit(score_text, (10, 10))

def increase_score(score, points=1):
    """
    Increases the score by a given number of points (default is 1).
    :param score: Current score
    :param points: Points to add
    :return: Updated score
    """
    return score + points

# Inside your main game loop
running = True
while running:
    # Game logic...

    # Check for collision with food
    if snake_head.colliderect(food_rect):
        score = increase_score(score)  # Increase score by 1
        # Spawn new food, grow snake, etc.

    # Drawing everything
    screen.fill((0, 0, 0))  # Clear screen with black
    draw_score(screen, score)  # Draw the score
    pygame.display.update()  # Update the display
