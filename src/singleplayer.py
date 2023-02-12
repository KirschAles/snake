import pygame
import pygame.locals
from world import World
from directions import Right, Left, Up, Down


def update(world: World, event) -> None:
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
    timer = pygame.time.Clock()
    timer.tick(60)

    canvas = pygame.display.set_mode((canvas_width, canvas_height))
    # game loop
    world = World(height, width)
    to_draw = []
    time_elapsed = 0
    while not exiting:
        canvas.fill(canvas_colour)
        time_elapsed += timer.tick(60)
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
            pygame.draw.rect(canvas,
                             drawing.colour,
                             pygame.Rect(drawing.x * block_size,
                                         drawing.y * block_size,
                                         block_size,
                                         block_size))
        pygame.display.update()
        if world.isgame_over:
            exiting = True
