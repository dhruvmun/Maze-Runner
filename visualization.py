import turtle
import maze

def setTurtle(turtleObject):
	turtleObject.speed(0)

def drawSquare(turtleObject, x, y, scale, fill):
	turtleObject.up()
	turtleObject.goto(x*scale, -y*scale)
	turtleObject.down()
	if fill :
		turtleObject.begin_fill()
	for i in range(4):
		turtleObject.forward(scale)
		turtleObject.left(90)
	if fill :
		turtleObject.end_fill()


def drawMaze(mazeObject, turtleObject, scale):
	for row in range(mazeObject.dimension):
		for column in range(mazeObject.dimension):
			drawSquare(turtleObject, column, row, scale, mazeObject.mazeCells[row][column] == 1)

def drawPath(path, turtleObject, scale, color):
	turtle.fillcolor(color)
	for (row, column) in path:
		drawSquare(turtleObject, column, row, scale, True)
			
