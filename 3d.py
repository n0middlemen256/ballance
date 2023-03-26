import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Define the ball properties
BALL_RADIUS = 0.2
BALL_START_X = 0
BALL_START_Y = 0
BALL_START_Z = 5
BALL_SPEED_X = 0.01
BALL_SPEED_Y = 0.01
BALL_SPEED_Z = 0
BALL_ACC_X = 0
BALL_ACC_Y = 0
BALL_ACC_Z = -0.001
BALL_MAX_SPEED = 0.1

# Define the balance beam properties
BEAM_WIDTH = 1
BEAM_HEIGHT = 0.1
BEAM_LENGTH = 10
BEAM_START_X = -BEAM_WIDTH / 2
BEAM_START_Y = -BEAM_LENGTH / 2
BEAM_START_Z = -BEAM_HEIGHT / 2

# Initialize Pygame and PyOpenGL
pygame.init()
pygame.display.set_caption("Ball Balance Game")
screen = pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
gluPerspective(45, (800 / 600), 0.1, 50.0)
glTranslatef(0.0, 0.0, -10)

# Set up the game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Move the ball
    BALL_SPEED_X += BALL_ACC_X
    BALL_SPEED_Y += BALL_ACC_Y
    BALL_SPEED_Z += BALL_ACC_Z
    if BALL_SPEED_X > BALL_MAX_SPEED:
        BALL_SPEED_X = BALL_MAX_SPEED
    if BALL_SPEED_Y > BALL_MAX_SPEED:
        BALL_SPEED_Y = BALL_MAX_SPEED
    if BALL_SPEED_Z < -BALL_MAX_SPEED:
        BALL_SPEED_Z = -BALL_MAX_SPEED
    BALL_START_X += BALL_SPEED_X
    BALL_START_Y += BALL_SPEED_Y
    BALL_START_Z += BALL_SPEED_Z

    # Check for collisions with the balance beam
    if BALL_START_X >= BEAM_START_X and \
            BALL_START_X <= BEAM_START_X + BEAM_WIDTH and \
            BALL_START_Y >= BEAM_START_Y and \
            BALL_START_Y <= BEAM_START_Y + BEAM_LENGTH:
        BALL_SPEED_Z = -BALL_SPEED_Z

    # Check for collisions with the screen edges
    if BALL_START_X - BALL_RADIUS <= -4 or BALL_START_X + BALL_RADIUS >= 4:
        BALL_SPEED_X = -BALL_SPEED_X
    if BALL_START_Y - BALL_RADIUS <= -3 or BALL_START_Y + BALL_RADIUS >= 3:
        BALL_SPEED_Y = -BALL_SPEED_Y
    if BALL_START_Z - BALL_RADIUS <= -10:
        BALL_SPEED_Z = -BALL_SPEED_Z

    # Clear the screen
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Draw the balance beam
    glBegin(GL_QUADS)
    glVertex3f(BEAM_START_X, BEAM_START_Y, BEAM_START_Z)
    glVertex3f(BEAM_START_X, BEAM_START_Y + BEAM_LENGTH, BEAM_START_Z)
    glVertex3f(BEAM_START_X + BEAM_WIDTH, BEAM_START_Y + BEAM_LENGTH, BEAM_START_Z)
    glVertex3f(BEAM_START_X + BEAM_WIDTH, BEAM_START_Y, BEAM_START_Z)
    glEnd()
    glColor3f(1.0, 0.0, 0.0)
    glPushMatrix()
    glTranslatef(BALL_START_X, BALL_START_Y, BALL_START_Z)
    quad = gluNewQuadric()
    gluQuadricDrawStyle(quad, GLU_FILL)
    gluQuadricNormals(quad, GLU_SMOOTH)
    gluSphere(quad, BALL_RADIUS, 32, 32)
    gluDeleteQuadric(quad)
    glPopMatrix()

    # Swap the buffers
    pygame.display.flip()


    # Draw the ball
