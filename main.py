import pygame

# Define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Define the screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Define the ball properties
BALL_RADIUS = 20
BALL_START_X = SCREEN_WIDTH // 2
BALL_START_Y = SCREEN_HEIGHT - 50
BALL_SPEED_X = 0
BALL_SPEED_Y = 0
BALL_ACC_X = 0.1
BALL_ACC_Y = 0.1
BALL_MAX_SPEED = 5

# Define the balance beam properties
BEAM_WIDTH = 200
BEAM_HEIGHT = 20
BEAM_START_X = SCREEN_WIDTH // 2 - BEAM_WIDTH // 2
BEAM_START_Y = SCREEN_HEIGHT - 100

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ball Balance Game")

# Set up the clock
clock = pygame.time.Clock()

# Create the ball sprite
ball = pygame.sprite.Sprite()
ball.image = pygame.Surface((BALL_RADIUS * 2, BALL_RADIUS * 2))
pygame.draw.circle(ball.image, RED, (BALL_RADIUS, BALL_RADIUS), BALL_RADIUS)
ball.rect = ball.image.get_rect()
ball.rect.x = BALL_START_X
ball.rect.y = BALL_START_Y

# Create the balance beam sprite
beam = pygame.sprite.Sprite()
beam.image = pygame.Surface((BEAM_WIDTH, BEAM_HEIGHT))
beam.image.fill(BLACK)
beam.rect = beam.image.get_rect()
beam.rect.x = BEAM_START_X
beam.rect.y = BEAM_START_Y

# Set up the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the ball
    BALL_SPEED_X += BALL_ACC_X
    BALL_SPEED_Y += BALL_ACC_Y
    if BALL_SPEED_X > BALL_MAX_SPEED:
        BALL_SPEED_X = BALL_MAX_SPEED
    if BALL_SPEED_Y > BALL_MAX_SPEED:
        BALL_SPEED_Y = BALL_MAX_SPEED
    ball.rect.x += BALL_SPEED_X
    ball.rect.y += BALL_SPEED_Y

    # Check for collisions with the balance beam
    if ball.rect.bottom >= beam.rect.top and \
            ball.rect.left <= beam.rect.right and \
            ball.rect.right >= beam.rect.left:
        BALL_SPEED_Y = -BALL_SPEED_Y

    # Check for collisions with the screen edges
    if ball.rect.left <= 0 or ball.rect.right >= SCREEN_WIDTH:
        BALL_SPEED_X = -BALL_SPEED_X
    if ball.rect.top <= 0:
        BALL_SPEED_Y = -BALL_SPEED_Y

    # Draw the sprites
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, (BEAM_START_X, BEAM_START_Y, BEAM_WIDTH, BEAM_HEIGHT))
    screen.blit(ball.image, ball.rect)
    pygame.display.flip()

    # Set the game clock
    clock.tick(60)

# Quit Pygame
pygame.quit()
