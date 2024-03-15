from enum import IntEnum


class Directions(IntEnum):
    N = 0
    E = 1
    S = 2
    W = 3


class MarsRover:
    def __init__(self) -> None:
        self.y_position = 0
        self.direction = Directions.N

    def execute(self, command: str) -> str:
        for action in command:
            if action == "M":
                self.y_position += 1
                self.y_position %= 10

            if action == "R":
                direction = self.direction + 1
                self.direction = Directions(direction)

        return f"0:{self.y_position}:{self.direction.name}"
