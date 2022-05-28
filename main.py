#   Paint Lite (only supports brush with black color) 
#   May 28, 2022

import pygame
from pygame.locals import *

WIDTH, HEIGHT = 800, 600
white = (255, 255, 255)
pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Paint Lite')

#   Icon
paintIcon = pygame.image.load('images/paintIcon.png')
pygame.display.set_icon(paintIcon)

#   Loading image
brushImg_unscaled = pygame.image.load('images/brush.png')

#   Resizes to new resolution
brushImg_scaled = pygame.transform.scale(brushImg_unscaled, (15, 15))

running = True
write = False

#   Fill screen with white color (default black)
win.fill(white)

while (running):
    #   Get mouse postion
    mx, my = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN: #   Mouse click
            write = True
        elif event.type == MOUSEBUTTONUP:   #   Mouse release
            write = False

        #   Displaying image
        if write:
            win.blit(brushImg_scaled, (mx, my))
            
    pygame.display.update()