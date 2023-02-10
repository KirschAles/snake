import pygame
import pygame.locals
from movable import MovableRect
import sys
from world import World


def update(world: World, event) -> list:
    if event.key == pygame.K_LEFT or event.key == ord('a'):
        world.move_player_left()
    if event.key == pygame.K_UP or event.key == ord('w'):
        world.move_player_up()
    if event.key == pygame.K_DOWN or event.key == ord('s'):
        world.move_player_down()
    if event.key == pygame.K_RIGHT or event.key == ord('d'):
        world.move_player_right()

    return world.draw()


width = 20
height = 20
block_size = 15
canvas_width = width * block_size
canvas_height = height * block_size
canvas_colour = (255, 255, 255)

pygame.init()

exiting = False
pygame.display.set_caption('My Game')
FPS = pygame.time.Clock()
FPS.tick(60)
canvas = pygame.display.set_mode((canvas_height, canvas_width))
# game loop
world = World(height, width)
to_draw = []
while not exiting:
    canvas.fill(canvas_colour)
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.locals.QUIT:
            exiting = True
        if event.type == pygame.locals.KEYDOWN:
            to_draw = update(world, event)
            if world.isgame_over:
                exiting = True
    for drawing in to_draw:
        pygame.draw.rect(canvas, drawing.colour, pygame.Rect(drawing.x * block_size, drawing.y * block_size, block_size, block_size))
    pygame.display.update()