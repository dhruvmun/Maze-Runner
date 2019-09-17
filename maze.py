import random;

class Maze:
	# bool flag;
	mazeCells =[]

	def generateMaze(dim, p):
		for i in range(dim):
			for j in range(dim):
				if (random.uniform(0, 1) <= p):
					mazeCells[i][j] = 1;
				else:
					mazeCells[i][j] = 0;
		return mazeCells;

	def giveEligibleChild(x, y, dim):
		tuple=[]
		if x-1 >= 0:
			if mazeCells[x-1][y]==1:
				tuple.append((x-1,y))
		if x+1<=dim-1:
			if mazeCells[x+1][y]==1:
				tuple.append((x+1,y))
		if y-1>=0:
			if mazeCells[x][y-1]==1:
				tuple.append((x,y-1))
		if y+1<=dim-1:
			if mazeCells[x][y+1]==1:
				tuple.append((x,y+1))
		return tuple
