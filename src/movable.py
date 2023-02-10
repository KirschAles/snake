from pygame import Rect
import pygame
import pygame.locals as key
from math import ceil

class Movable:
    def __init__(self, x_pos: int, y_pos: int):
        self.x = x_pos
        self.y = y_pos

    def move(self, x_change: float = 0, y_change: float = 0):
        self.x = ceil(self.x + x_change)
        self.y = ceil(self.y + y_change)

    def move_left(self, left_change: int):
        self.move(-left_change, 0)

    def move_right(self, right_change: int):
        self.move(right_change)

    def move_up(self, up_change: int):
        self.move(0, -up_change)

    def move_down(self, down_change: int):
        self.move(0, down_change)


class MovableRect(Movable):
    base_speed = 1

    def __init__(self,
                 x_pos: int,
                 y_pos: int,
                 width: int,
                 height: int):
        super().__init__(x_pos, y_pos)
        self.width = width
        self.height = height
        self.speed = ceil(self.base_speed*width)

    def get_draw(self):
        return Rect(self.x, self.y, self.width, self.height)

    def left(self):
        super().move_left(self.speed)

    def right(self):
        super().move_right(self.speed)

    def up(self):
        super().move_up(self.speed)

    def down(self):
        super().move_down(self.speed)

    def update(self, event):
        if event.key == pygame.K_LEFT or event.key == ord('a'):
            self.left()
        if event.key == pygame.K_UP or event.key == ord('w'):
            self.up()
        if event.key == pygame.K_DOWN or event.key == ord('s'):
            self.down()
        if event.key == pygame.K_RIGHT or event.key == ord('d'):
            self.right()

    def __str__(self):
        return str(self.x) + ', ' + str(self.y)