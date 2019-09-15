import random;
from collections import defaultdict;

class Maze:
	# bool flag;
	mazeCells = {};

def generateMaze(dim, p):
	mazeCells = defaultdict(list);
	for i in range(dim):
		for j in range(dim):
			if(random.uniform(0,1) < p):
				mazeCells[i].append(j);
	return mazeCells;

mazeCells = generateMaze(10,0.6);
for i in range(10):
	print (str(i)  + mazeCells[i])
# print(mazeCells)
