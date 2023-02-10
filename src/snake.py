import numpy as np
from position import Position


class Snake:
    def __init__(self, position):
        self.parts = []
        self.parts.append(SnakePart(position))

    def move_to(self, position):
        curr_position = position

        # moves all body parts forward, last position is lost
        for part in reversed(self.parts):
            temp_position = part.position
            part.position = curr_position
            curr_position = temp_position

    def grow_to(self, position):
        self.parts.append(SnakePart(position))

    def head(self):
        return self.parts[-1].position

    def collides_with(self, position) -> bool:
        for part in self.parts:
            print(part.position)
            if position == part.position:
                return True
        return False

    def draw(self):
        drawing = []
        for part in self.parts:
            drawing.append(part.draw())
        return drawing


class SnakePart:
    colour = 'green'

    def __init__(self, position: Position):
        self._position = position
        self._position.colour = self.colour

    @property
    def position(self) -> Position:
        return self._position

    @position.setter
    def position(self, position: Position):
        position.colour = self.colour
        self._position = position

    def draw(self):
        return self.position