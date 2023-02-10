import pygame
import pygame.locals
from movable import MovableRect
import sys

pygame.init()

color = (255, 255, 255)
rect_color = (255, 0, 0)

exiting = False
pygame.display.set_caption('My Game')
FPS = pygame.time.Clock()
FPS.tick(60)
canvas = pygame.display.set_mode((500, 500))
# game loop
rect = MovableRect(0, 0, 60, 60)
while not exiting:
    canvas.fill(color)
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.locals.QUIT:
            exiting = True
        if event.type == pygame.locals.KEYDOWN:
            print('here')
            rect.update(event)
    pygame.draw.rect(canvas, rect_color, rect.get_draw())
    pygame.display.update()