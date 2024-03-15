class MarsRover:
    def __init__(self) -> None:
        self.y_position = 0

    def execute(self, command: str) -> str:
        if command == "M":
            self.y_position += 1
        return f"0:{self.y_position}:N"
