import turtle
import maze

class Visualize:

	def __init__(self, title, color, bx, by):
		self.turtleObject = turtle.Turtle()
		self.screenObject = turtle.Screen()
		self.screenObject.title(title)
		self.turtleObject.speed(0)
		self.scale = 15
		self.pathColor = color
		self.basex = bx
		self.basey = by

	def drawSquare(self, x, y, fill):
		self.turtleObject.up()
		self.turtleObject.goto(self.basex+x*self.scale, self.basey-y*self.scale)
		self.turtleObject.down()
		if fill :
			self.turtleObject.begin_fill()
		for i in range(4):
			self.turtleObject.forward(self.scale)
			self.turtleObject.left(90)
		if fill :
			self.turtleObject.end_fill()


	def drawMaze(self, mazeObject):
		for row in range(mazeObject.dimension):
			for column in range(mazeObject.dimension):
				self.drawSquare(column, row, mazeObject.mazeCells[row][column] == 1)

	def drawPath(self, path):
		self.turtleObject.fillcolor(self.pathColor)
		for (row, column) in path:
			self.drawSquare(column, row, True)
		self.turtleObject.ht()
			
