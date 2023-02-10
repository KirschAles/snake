class Position:
    def __init__(self, position: tuple, colour: str = 'red'):
        self._x = position[0]
        self._y = position[1]
        self._colour = colour

    def left(self):
        return Position((self._x - 1, self._y))

    def right(self):
        return Position((self._x + 1, self._y))

    def up(self):
        return Position((self._x, self._y - 1))

    def down(self):
        return Position((self._x, self._y + 1))

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def colour(self):
        return self._colour

    @colour.setter
    def colour(self, colour: str):
        self._colour = colour

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return str(self.x) + ', ' + str(self.y) + '  ' + self.colour
