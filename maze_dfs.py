import random
from collections import defaultdict

class Maze:
	# bool flag
	mazeCells = {}

def generateMaze(dim, p):
	mazeCells = []
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


def give_eligible_child(x,y):
# Expand Children of State
	if(x-1 > 0):
		fringe.append((x-1,y,path))
	if(x+1 < dims):
		fringe.append((x+1,y,path))
	if(y-1 > 0):
		fringe.append((x,y-1,path))
	if(y+1 < dims):
		fringe.append((x,y+1,path))


def dfs(dims,cs):

	goal_state = (dims-1,dims-1)
	fringe = [(0,0,[0,0])] #x,y,path
	closed_set = cs
	
	while (len(fringe)):
		x,y,path = fringe.pop()
		current_state = (x,y)

		if(current_state not in closed_set):
			path.append(current_state)
			#print(current_state)

			if (current_state == goal_state):
				return path

			give_child(x,y)

			closed_set.append(current_state)
	return "NO SOLUTION"


cs = [(1,1),(2,0),(0,3),(1,4),(3,3),(4,2)]
x = dfs(5,cs)
print(x)