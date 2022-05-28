import pygame
from pygame.locals import *

pygame.init()
win = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Paint Lite')

running = True

while (running):
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
    pygame.display.update()
            