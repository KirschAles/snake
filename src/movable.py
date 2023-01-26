from pygame import Rect


class Movable:
    def __init__(self, x_pos: int, y_pos: int):
        self.x = x_pos
        self.y = y_pos

    def move(self, x_change, y_change):
        self.x = self.x + x_change
        self.y = self.y + y_change

    def move_left(self, left_change):
        self.move(-left_change, 0)

    def move_right(self, right_change):
        self.move(right_change)

    def move_up(self, up_change):
        self.move(0, -up_change)

    def move_down(self, down_change):
        self.move(0, down_change)


class MovableRect(Movable):
    def __init__(self,
                 x_pos: int,
                 y_pos: int,
                 width: int,
                 height: int):
        super().__init__(x_pos, y_pos)
        self.width = width
        self.height = height

    def get_draw(self):
        return Rect(self.x, self.y, self.width, self.height)