import maze
import helper
import heapq
import matplotlib.pyplot as plt
import random

def giveFireChild(x, y, q, k):
	'''
	calculate fire probability by the given formula
	parameters: x,y - coordinates of current cell
				q - flamability
				k - number of neighbours in fire
	return: boolean value if the cell (x,y) is on fire
	'''
	fireProb = 1-pow((1-q),k)
	if (random.uniform(0, 1) <= fireProb):
		return True
	else:
		return False


def expandFire(mazeObject, fireset, q):
	'''
	function to expand fire at each time step
	parameters: mazeObject
				fireset - List of cells on fire
				q - flamability
	returns: Updated fireset
	'''
	oldMazeObject = mazeObject
	mazeObject = maze.Maze(oldMazeObject.dimension, oldMazeObject.probability)
	for i in range(mazeObject.dimension):
		for j in range(mazeObject.dimension):
			mazeObject.mazeCells[i][j] = oldMazeObject.mazeCells[i][j]
			if(mazeObject.mazeCells[i][j] == 0):
				k = oldMazeObject.giveFireNeighbours(i,j)
				if(k==0):
					continue
				else:
					if(giveFireChild(i, j, q, k)):
						fireset.append((i,j))
						mazeObject.mazeCells[i][j] = 2
	return (fireset, mazeObject)

def aStarSearch(mazeObject, distanceFunction, startx,starty, endx , endy):
	'''
	An A* search function to calculate the shortest path
	'''
	path = {}
	fringe = [(0,(startx,starty, (-1, -1, 0)))]
	closedSet = []
	while (len(fringe) != 0):
		(heuristicValue,(x, y, (parentx,parenty,pathLength))) = heapq.heappop(fringe)
		if (x,y) not in closedSet:
			if (x,y) == (endx,endy):
				path[(x,y)] = (parentx,parenty)
				return mazeObject.getPath(path, endx, endy)
			eligibleChildren = mazeObject.giveEligibleChild(x,y);
			for (cx,cy) in eligibleChildren:
				heuristic = distanceFunction(cx,cy,endx,endy)+pathLength
				heapq.heappush(fringe,(heuristic,(cx,cy,(x,y,pathLength+1))))
			closedSet.append((x,y))
			path[(x,y)] = (parentx,parenty)
	return []

def findPath(p,q):
	'''
	parameters: p - probability of blocked cell in maze
				q - flamability rate
	returns: 0 - Dead
			 1 - Success
	
	shortestPath_fire: shortest path from top right to bottom left
	shortestPath: shortest path from top left to bottom right
	fireset: List of cells on fire
	'''
	shortestPath_fire = []
	shortestPath = []
	'''
	Generate Maze such that path exists from top right to bottom & left top left to bottom right
	mazeCell values: 0-> Open, 1-> Block, 2-> Fire
	'''
	while (shortestPath_fire == [] or shortestPath == []):
		mazeObject = maze.Maze(dim, p)
		shortestPath_fire = aStarSearch(mazeObject, helper.manhattanDistance, 0,dim-1, dim-1,0)
		shortestPath = aStarSearch(mazeObject, helper.manhattanDistance, 0,0, dim-1,dim-1)
	#Initialize fire on top right corner cell.
	mazeObject.mazeCells[0][dim-1] = 2
	fireset = [(0,dim-1)]

	while shortestPath != []:
		'''
		Move along the shortest path gernerated above and expand fire in each step
		If runner crosses fire state return dead
		'''
		next_step = shortestPath.pop(0)
		(fireset, mazeObject) = expandFire(mazeObject, fireset, q)
		if next_step in fireset:
			return 0  #"Dead"
	return 1  #"Success"

def plotgraph():
	'''
	function to plot graph between the flamability rate and avg success
	'''
	plt.plot(qs, avgsuccess)
	plt.xlabel('flamability')
	plt.ylabel('avg Success')
	plt.title('flamability vs success')
	plt.show()


dim = 100
qs = []		#List of range of q values from 0-1
for i in range(11):
	qs.append(float(i)/10)
no_of_maze_per_q = 50
avgsuccess = []
for q in qs:
	'''
	q: flamability
	d: death count
	s: survival count
	'''
	d=0 
	s=0
 	for i in range(no_of_maze_per_q):
 		a = findPath(0.2,q)
 		if a==0:
 			d+=1
 		elif a==1:
 			s+=1
	avgsuccess.append(float(s)/(s+d))

plotgraph()
