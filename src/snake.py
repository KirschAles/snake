import numpy as np


class Snake:
    def __init__(self, position):
        self.parts = []
        self.parts.append(SnakePart(position))

    def move_to(self, position):
        curr_position = position

        # moves all body parts forward, last position is lost
        for part in reversed(self.parts):
            temp_position = part.position()
            part.change_position(curr_position)
            curr_position = temp_position

    def grow_to(self, position):
        self.parts.append(SnakePart(position))
        

class SnakePart:
    def __init__(self, position: tuple):
        self._x = position[0]
        self._y = position[1]

    def change_position(self, position: tuple):
        self._x = position[0]
        self._y = position[1]

    def position(self) -> tuple:
        return self._x, self._y