class MarsRover:
    def __init__(self) -> None:
        self.y_position = 0
        self.direction = 'N'

    def execute(self, command: str) -> str:
        for action in command:
            if action == "M":
                self.y_position += 1
                self.y_position %= 10
            if action == 'R':
                self.direction = 'E'

        return f"0:{self.y_position}:{self.direction}"
