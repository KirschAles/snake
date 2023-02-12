import pygame.locals
import pygame_gui
from singleplayer import game_loop


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
