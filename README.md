# toy-robot-code-exam

#### Project Description

The application is a simulation of a toy robot moving on a square table top, of dimensions 5 units x 5 units. There are no
other obstructions on the table surface. The robot is free to roam around the surface of the table, but must be prevented
from falling to destruction. Any movement that would result in the robot falling from the table must be prevented,
however further valid movement commands must still be allowed.

#### Project Requirements
Create a console application that can read in commands of the following form -
PLACE X,Y,F
MOVE
LEFT
RIGHT
REPORT
PLACE will put the toy robot on the table in position X,Y and facing NORTH, SOUTH, EAST or WEST. The origin (0,0)
can be considered to be the SOUTH WEST most corner. It is required that the first command to the robot is a PLACE
command, after that, any sequence of commands may be issued, in any order, including another PLACE command. The
application should discard all commands in the sequence until a valid PLACE command has been executed.
MOVE will move the toy robot one unit forward in the direction it is currently facing.
LEFT and RIGHT will rotate the robot 90 degrees in the specified direction without changing the position of the robot.
REPORT will announce the X,Y and F of the robot. This can be in any form, but standard output is sufficient.
A robot that is not on the table can choose to ignore the MOVE, LEFT, RIGHT and REPORT commands.
Input can be from a file, or from standard input, as the developer chooses.

#### Test and Error Handling
Provide test data to exercise the application.
It is not required to provide any graphical output showing the movement of the toy robot.
The application should handle error states appropriately and be robust to user input.

#### Installation

Steps to Run the Python Script
1. Save the Main Script:
- Save the main Python script as toy_robot.py.

2. Run the Script:
- Open a terminal or command prompt and navigate to the directory where you saved the file.
- Run the script with the following command: python toy_robot.py

3. Run Unit Tests:
- Save the unit test file (unittest.py) in the same directory.
- To run the tests, use the following command in the terminal: python -m unittest unittest.py

