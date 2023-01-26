import pygame
import pygame.locals
import sys

pygame.init()

color = (255, 255, 255)
rect_color = (255, 0, 0)

exiting = False
pygame.display.set_caption('My Game')

canvas = pygame.display.set_mode((500, 500))
# game loop
while not exiting:
    canvas.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            exiting = True

    pygame.draw.rect(canvas, rect_color, pygame.Rect(200, 200, 100, 100))
    pygame.display.update()