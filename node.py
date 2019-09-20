import maze;

class Node:

	def __init__(self, xc, yc, p, l):
		self.x = xc;
		self.y = yc;
		self.parent = p;
		self.pathLength = l;