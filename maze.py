import random;

class Maze:
	# int dimension;
	# float probability;
	# list mazeCells;

	def __init__(self, dim, p):
		self.dimension = dim;
		self.probability = p;
		self.mazeCells = [];
		for i in range(self.dimension):
			self.mazeCells.append([]);
			for j in range(self.dimension):
				if (random.uniform(0, 1) <= self.probability):
					self.mazeCells[i].append(1);
				else:
					self.mazeCells[i].append(0);
		self.mazeCells[0][0] = 0;
		self.mazeCells[dimension-1][dimension-1] = 0;

	def giveEligibleChild(self, x, y):
		children=[]
		if x-1 >= 0:
			if self.mazeCells[x-1][y]==1:
				children.append((x-1,y))
		if x+1<=self.dimension-1:
			if self.mazeCells[x+1][y]==1:
				children.append((x+1,y))
		if y-1>=0:
			if self.mazeCells[x][y-1]==1:
				children.append((x,y-1))
		if y+1<=self.dimension-1:
			if self.mazeCells[x][y+1]==1:
				children.append((x,y+1))
		return children;

