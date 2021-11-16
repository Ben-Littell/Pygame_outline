import pygame
import math
import random

# colors in RGB
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
COLORS = [RED, GREEN, BLUE, BLACK]

# Math Constants
PI = math.pi

# Game Constants
WIDTH = 700
HEGHT = 500
SIZE = (WIDTH, HEIGHT)
FPS = 60

##############################################################################
##############################################################################

pygame.init()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Animation Intro')

clock = pygame.time.Clock()

running = True
########################################################################################################################

########################################################################################################################
# game loop
while running:
    # get all mouse, keyboard, controller events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    pygame.display.flip()

    clock.tick(FPS)

# outside of game loop
pygame.quit()







