from enum import IntEnum


class Directions(IntEnum):
    N = 0
    E = 1
    S = 2
    W = 3


class MarsRover:
    def __init__(self) -> None:
        self.x_position = 0
        self.y_position = 0
        self.direction = Directions.N

    def __rotate_left(self) -> None:
        self.direction = Directions((self.direction - 1) % 4)

    def __rotate_right(self) -> None:
        self.direction = Directions((self.direction + 1) % 4)

    def __move(self) -> None:
        if self.direction == Directions.N:
            self.y_position += 1
            self.y_position %= 10

        if self.direction == Directions.S:
            self.y_position -= 1
            self.y_position %= 10

        if self.direction == Directions.E:
            self.x_position += 1
            self.x_position %= 10

        if self.direction == Directions.W:
            self.x_position -= 1
            self.x_position %= 10

    def execute(self, command: str) -> str:
        for action in command:
            if action == "R":
                self.__rotate_right()

            if action == "L":
                self.__rotate_left()

            if action == "M":
                self.__move()

        return f"{self.x_position}:{self.y_position}:{self.direction.name}"
