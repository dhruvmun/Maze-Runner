import random;
from collections import defaultdict;

class Maze:
	# bool flag;
	mazeCells = {};

def generateMaze(dim, p):
	mazeCells = [];
	for i in range(dim):
		mazeCells.append([]);
		for j in range(dim):
			if(random.uniform(0,1) <= p):
				mazeCells[i].append(1);
			else:
				mazeCells[i].append(0);
	return mazeCells;

mazeCells = generateMaze(10,0.6);
for i in range(10):
	print (str(i) + ":"  + str(mazeCells[i]));
