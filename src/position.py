class Position:
    def __init__(self, position: tuple):
        self._x = position[0]
        self._y = position[1]

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