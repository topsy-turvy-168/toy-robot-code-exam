class ToyRobotError(Exception):
    """Custom exception for ToyRobot."""
    pass

class Board:
    def __init__(self, width, height):
        """Create a board with given width and height."""
        self.width = width
        self.height = height

    def is_valid_position(self, x, y):
        """Check if the given (x, y) position is within the board boundaries."""
        return 0 <= x < self.width and 0 <= y < self.height

class ToyRobot:
    DIRECTIONS = ['NORTH', 'EAST', 'SOUTH', 'WEST']

    def __init__(self, board):
        """Initialize the robot on the given board."""
        self.board = board
        self.x = None
        self.y = None
        self.facing = None

    def place(self, x, y, facing):
        """Place the robot on the board at a valid position and facing a valid direction."""
        if not self.board.is_valid_position(x, y):
            raise ToyRobotError(f"Invalid position: ({x}, {y}) is out of bounds")
        if facing not in ToyRobot.DIRECTIONS:
            raise ToyRobotError(f"Invalid direction: {facing}")
        self.x = x
        self.y = y
        self.facing = facing

    def move(self):
        """Move the robot one unit forward in the direction it's facing."""
        if self.facing == 'NORTH' and self.board.is_valid_position(self.x, self.y + 1):
            self.y += 1
        elif self.facing == 'EAST' and self.board.is_valid_position(self.x + 1, self.y):
            self.x += 1
        elif self.facing == 'SOUTH' and self.board.is_valid_position(self.x, self.y - 1):
            self.y -= 1
        elif self.facing == 'WEST' and self.board.is_valid_position(self.x - 1, self.y):
            self.x -= 1
        else:
            raise ToyRobotError("Move would take the robot off the board")

    def left(self):
        """Turn the robot left."""
        self.facing = ToyRobot.DIRECTIONS[(ToyRobot.DIRECTIONS.index(self.facing) - 1) % 4]

    def right(self):
        """Turn the robot right."""
        self.facing = ToyRobot.DIRECTIONS[(ToyRobot.DIRECTIONS.index(self.facing) + 1) % 4]

    def report(self):
        """Report the current position and facing direction of the robot."""
        if self.x is None or self.y is None or self.facing is None:
            raise ToyRobotError("Robot is not placed yet")
        return f"{self.x},{self.y},{self.facing}"


if __name__ == "__main__":
    # Create a 5x5 board
    board = Board(5, 5)

    # Create a robot and place it on the board
    robot = ToyRobot(board)
    robot.place(0, 0, 'NORTH')
    robot.move()
    robot.right()
    robot.move()
    
    # Report the robot's position
    print(robot.report())  # Expected output: "1,1,EAST"
