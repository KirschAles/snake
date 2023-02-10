from snake import Snake
from position import Position
import random


def random_position(width: int, height: int) -> Position:
    x = random.randint(0, width - 1)
    y = random.randint(0, height - 1)
    return Position((x, y))


class World:

    def __init__(self, height: int, width: int):
        self.height = height
        self.width = width

        self.player = Snake(Position((0, 0)))
        self.bait = self.new_bait()
        self.isgame_over = False

    def move_player_left(self):
        return self.move_player_to(self.player.head().left())

    def move_player_right(self):
        return self.move_player_to(self.player.head().right())

    def move_player_up(self):
        return self.move_player_to(self.player.head().up())

    def move_player_down(self):
        return self.move_player_to(self.player.head().down())

    def move_player_to(self, position: Position) -> bool:
        if position == self.bait:
            self.player.grow_to(position)
            self.bait = self.new_bait()
        else:
            self.player.move_to(position)
        self.isgame_over = self.player.collides_with_itself()

    def new_bait(self):
        new_bait = random_position(self.width, self.height)
        while self.player.collides_with(new_bait):
            new_bait = random_position(self.width, self.height)
        print(new_bait)
        return new_bait

    def draw(self):
        objects = []
        objects.extend(self.player.draw())
        objects.append(self.bait)
        return objects