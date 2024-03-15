from src.mars_rover import MarsRover


def test_should_construct_class():
   mars_rover = MarsRover([[]])

   assert isinstance(mars_rover, MarsRover)

def test_should_start_initial_position():
   mars_rover = MarsRover([[]])

   result = mars_rover.execute("")

   assert result == "0:0:N"
