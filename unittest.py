import unittest

class TestToyRobot(unittest.TestCase):

    def setUp(self):
        # Create a 5x5 board and initialize the robot
        self.board = Board(5, 5)
        self.robot = ToyRobot(self.board)

    def test_place_robot(self):
        self.robot.place(0, 0, 'NORTH')
        self.assertEqual(self.robot.report(), "0,0,NORTH")

    def test_invalid_placement(self):
        with self.assertRaises(ToyRobotError):
            self.robot.place(-1, 0, 'NORTH')
        with self.assertRaises(ToyRobotError):
            self.robot.place(0, 0, 'UP')

    def test_move_robot(self):
        self.robot.place(0, 0, 'NORTH')
        self.robot.move()
        self.assertEqual(self.robot.report(), "0,1,NORTH")

    def test_turn_left(self):
        self.robot.place(0, 0, 'NORTH')
        self.robot.left()
        self.assertEqual(self.robot.report(), "0,0,WEST")

    def test_turn_right(self):
        self.robot.place(0, 0, 'NORTH')
        self.robot.right()
        self.assertEqual(self.robot.report(), "0,0,EAST")

    def test_move_off_board(self):
        self.robot.place(0, 0, 'SOUTH')
        with self.assertRaises(ToyRobotError):
            self.robot.move()

    def test_report_before_placement(self):
        with self.assertRaises(ToyRobotError):
            self.robot.report()

if __name__ == '__main__':
    unittest.main()
