import pygame
import pygame.locals
import pygame_gui
from movable import MovableRect
import sys
from world import World
from directions import Right, Left, Up, Down


def update(world: World, event) -> list:
    if event.key == pygame.K_LEFT or event.key == ord('a'):
        world.player.orientation = Left()
    if event.key == pygame.K_UP or event.key == ord('w'):
        world.player.orientation = Up()
    if event.key == pygame.K_DOWN or event.key == ord('s'):
        world.player.orientation = Down()
    if event.key == pygame.K_RIGHT or event.key == ord('d'):
        world.player.orientation = Right()


def game_loop(canvas_height: int,
              canvas_width: int,
              canvas_colour: tuple,
              height: int,
              width: int,
              block_size: int,
              blocks_per_second: float):
    exiting = False
    FPS = pygame.time.Clock()
    FPS.tick(60)

    canvas = pygame.display.set_mode((canvas_width, canvas_height))
    # game loop
    world = World(height, width)
    to_draw = []
    time_elapsed = 0
    while not exiting:
        canvas.fill(canvas_colour)
        time_elapsed += FPS.tick(60)
        while time_elapsed >= 1000 * 1/blocks_per_second:
            world.move_player()
            time_elapsed -= 1000 * 1/blocks_per_second

        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                exiting = True
            if event.type == pygame.locals.KEYDOWN:
                update(world, event)

        to_draw = world.draw()
        for drawing in to_draw:
            pygame.draw.rect(canvas, drawing.colour, pygame.Rect(drawing.x * block_size, drawing.y * block_size, block_size, block_size))
        pygame.display.update()
        if world.isgame_over:
            exiting = True


width = 20
height = 15
block_size = 40
blocks_per_second = 5
canvas_width = width * block_size
canvas_height = height * block_size
canvas_colour = (200, 200, 200)


pygame.init()

window_surface = pygame.display.set_mode((canvas_width, canvas_height))
pygame.display.set_caption('Snake')
background = pygame.Surface((canvas_width, canvas_height))
background.fill(pygame.Color('#000000'))
manager = pygame_gui.UIManager((canvas_width, canvas_height))

single_player = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 200), (200, 50)),
                                            text='Single Player',
                                            manager=manager)
exit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 260), (200, 50)),
                                           text='Exit',
                                           manager=manager)

exiting = False
clock = pygame.time.Clock()

while not exiting:
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            exiting = True
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == single_player:
                game_loop(canvas_height,
                          canvas_width,
                          canvas_colour,
                          height,
                          width,
                          block_size,
                          blocks_per_second)
            if event.ui_element == exit_button:
                exiting = True
        manager.process_events(event)

    manager.update(time_delta)
    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)
    pygame.display.update()
