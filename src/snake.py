import numpy as np
from position import Position
import directions


class Snake:
    def __init__(self, position: Position):
        self.parts = []
        self.parts.append(SnakePart(position))
        self._orientation = directions.Right()

    @property
    def orientation(self) -> directions.Direction:
        return self._orientation

    @orientation.setter
    def orientation(self, orientation: directions.Direction) -> None:
        if len(self.parts) < 2 or self.pos_in_direction(orientation) != self.parts[-2].position:
            self._orientation = orientation

    def move(self) -> None:
        self.move_to(self.next_head_pos())

    def pos_in_direction(self, direction: directions.Direction) -> Position:
        if isinstance(direction, directions.Left):
            return self.head().left()
        elif isinstance(direction, directions.Right):
            return self.head().right()
        elif isinstance(direction, directions.Up):
            return self.head().up()
        elif isinstance(direction, directions.Down):
            return self.head().down()
        else:
            raise ValueError('Invalid snake orientation.')

    def next_head_pos(self) -> Position:
        return self.pos_in_direction(self.orientation)

    def move_to(self, position: Position) -> None:
        curr_position = position

        # moves all body parts forward, last position is lost
        for part in reversed(self.parts):
            temp_position = part.position
            part.position = curr_position
            curr_position = temp_position

    def grow_to(self, position: Position) -> None:
        self.parts.append(SnakePart(position))

    def head(self) -> Position:
        return self.parts[-1].position

    def collides_with(self, position: Position) -> bool:
        for part in self.parts:
            if position == part.position:
                return True
        return False

    def collides_with_itself(self) -> bool:
        for part in self.parts[0:len(self.parts)-1]:
            if part.position == self.head():
                return True
        return False

    def draw(self) -> list:
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
    def position(self, position: Position) -> None:
        position.colour = self.colour
        self._position = position

    def draw(self) -> Position:
        return self.position