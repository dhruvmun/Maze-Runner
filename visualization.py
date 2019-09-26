import turtle
import maze
from PIL import Image
import io
import os

class Visualize:

	def __init__(self, title, color, bx = 0, by = 0):
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

	def drawPath(self, path, color = 'yellow'):
		self.turtleObject.fillcolor(color)
		for (row, column) in path:
			self.drawSquare(column, row, True)
		self.turtleObject.ht()
			
	def exportPng(self, fileName):
		canvas = self.turtleObject.getscreen().getcanvas()
		psImage = canvas.postscript(file=fileName+'.ps')
		pngImage = Image.open(fileName+'.ps')
		pngImage.save(fileName+'.png', 'png')
		os.remove(fileName+'.ps')

	def clearScreen(self):
		self.turtleObject.clear()