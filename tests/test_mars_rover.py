from src.mars_rover import MarsRover


def test_should_construct_class() -> None:
    mars_rover = MarsRover()

    assert isinstance(mars_rover, MarsRover)


def test_should_start_initial_position() -> None:
    mars_rover = MarsRover()

    result = mars_rover.execute("")

    assert result == "0:0:N"


def test_should_rotate_right() -> None:
    mars_rover = MarsRover()

    result = mars_rover.execute("R")

    assert result == "0:0:E"


def test_should_rotate_right_two_times() -> None:
    mars_rover = MarsRover()

    result = mars_rover.execute("RR")

    assert result == "0:0:S"


def test_should_rotate_right_three_times() -> None:
    mars_rover = MarsRover()

    result = mars_rover.execute("RRR")

    assert result == "0:0:W"


def test_should_rotate_right_four_times() -> None:
    mars_rover = MarsRover()

    result = mars_rover.execute("RRRR")

    assert result == "0:0:N"


def test_should_rotate_left() -> None:
    mars_rover = MarsRover()

    result = mars_rover.execute("L")

    assert result == "0:0:W"


def test_should_rotate_left_two_times() -> None:
    mars_rover = MarsRover()

    result = mars_rover.execute("LL")

    assert result == "0:0:S"


def test_should_rotate_left_three_times() -> None:
    mars_rover = MarsRover()

    result = mars_rover.execute("LLL")

    assert result == "0:0:E"


def test_should_rotate_left_four_times() -> None:
    mars_rover = MarsRover()

    result = mars_rover.execute("LLLL")

    assert result == "0:0:N"


def test_should_move_y_axis_north() -> None:
    mars_rover = MarsRover()

    result = mars_rover.execute("M")

    assert result == "0:1:N"


def test_should_move_y_axis_north_two_times() -> None:
    mars_rover = MarsRover()

    result = mars_rover.execute("MM")

    assert result == "0:2:N"


def test_should_move_y_axis_north_ten_times() -> None:
    mars_rover = MarsRover()

    result = mars_rover.execute("MMMMMMMMMM")

    assert result == "0:0:N"


def test_should_move_y_axis_south() -> None:
    mars_rover = MarsRover()

    result = mars_rover.execute("RRM")

    assert result == "0:9:S"


def test_should_move_y_axis_south_two_times() -> None:
    mars_rover = MarsRover()

    result = mars_rover.execute("RRMM")

    assert result == "0:8:S"


def test_should_move_y_axis_south_ten_times() -> None:
    mars_rover = MarsRover()

    result = mars_rover.execute("RRMMMMMMMMMM")

    assert result == "0:0:S"


def test_should_move_x_axis_east() -> None:
    mars_rover = MarsRover()

    result = mars_rover.execute("RM")

    assert result == "1:0:E"


def test_should_move_x_axis_east_two_times() -> None:
    mars_rover = MarsRover()

    result = mars_rover.execute("RMM")

    assert result == "2:0:E"


def test_should_move_x_axis_east_ten_times() -> None:
    mars_rover = MarsRover()

    result = mars_rover.execute("RMMMMMMMMMM")

    assert result == "0:0:E"


def test_should_move_x_axis_west() -> None:
    mars_rover = MarsRover()

    result = mars_rover.execute("LM")

    assert result == "9:0:W"


def test_should_move_x_axis_west_two_times() -> None:
    mars_rover = MarsRover()

    result = mars_rover.execute("LMM")

    assert result == "8:0:W"


def test_should_move_x_axis_west_ten_times() -> None:
    mars_rover = MarsRover()

    result = mars_rover.execute("LMMMMMMMMMM")

    assert result == "0:0:W"


def test_should_move_in_circle_right() -> None:
    mars_rover = MarsRover()

    result = mars_rover.execute("MRMRMRM")

    assert result == "0:0:W"


def test_should_move_in_circle_left() -> None:
    mars_rover = MarsRover()

    result = mars_rover.execute("MLMLMLM")

    assert result == "0:0:E"
