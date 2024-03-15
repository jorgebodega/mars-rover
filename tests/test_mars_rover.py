from src.mars_rover import MarsRover


def test_should_construct_class() -> None:
    mars_rover = MarsRover()

    assert isinstance(mars_rover, MarsRover)


def test_should_start_initial_position() -> None:
    mars_rover = MarsRover()

    result = mars_rover.execute("")

    assert result == "0:0:N"


def test_should_move_y_axis() -> None:
    mars_rover = MarsRover()

    result = mars_rover.execute("M")

    assert result == "0:1:N"


def test_should_move_y_axis_twice() -> None:
    mars_rover = MarsRover()

    result = mars_rover.execute("MM")

    assert result == "0:2:N"


def test_should_move_y_axis_until_overflow() -> None:
    mars_rover = MarsRover()

    result = mars_rover.execute("MMMMMMMMMM")

    assert result == "0:0:N"
