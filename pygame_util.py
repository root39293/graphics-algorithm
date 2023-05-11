import pygame
import sys

def initialize_pygame(width, height, font_size):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, font_size)
    return screen, clock, font

def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def update_screen():
    pygame.display.flip()
    pygame.time.Clock().tick(60)
