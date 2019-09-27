import maze
import helper
import matplotlib.pyplot as plt
import random;
import heapq;
import helper;

class Maze:
	def __init__(self, dim, p):
		'''
		parameters: int dim- dimension;
					float p- probability;
					matrix mazeCells;
		Returns the mazeObject for a given value of dim and p
		'''
		self.dimension = dim
		self.probability = p
		self.mazeCells = []
		for i in range(self.dimension):
			self.mazeCells.append([])
			for j in range(self.dimension):
				if (random.uniform(0, 1) <= self.probability):
					self.mazeCells[i].append(1)
				else:
					self.mazeCells[i].append(0)
		self.mazeCells[0][0] = 0
		self.mazeCells[self.dimension-1][self.dimension-1] = 0

	def giveEligibleChild(self, x, y):
		'''
		parameters: x and y coordinate of the current state
		return: all the eligible children for that state.

		Checks for boundry condition and that child node is empty
		that is not a block or in closed state. 
		'''
		children=[]
		if x-1 >= 0:
			if self.mazeCells[x-1][y]==0:
				children.append((x-1,y))
		if x+1<=self.dimension-1:
			if self.mazeCells[x+1][y]==0:
				children.append((x+1,y))
		if y-1>=0:
			if self.mazeCells[x][y-1]==0:
				children.append((x,y-1))
		if y+1<=self.dimension-1:
			if self.mazeCells[x][y+1]==0:
				children.append((x,y+1))
		return children
	
	def aStarSearch(self, distanceFunction):
		'''
		An A* search function to calculate the shortest path
		input: mazeObject and distanceFunction- Manhattan/Euclid
		returns: length of max fringe size and
				 length of closedSet
		'''
		(startx, starty) = (0,0)
		(endx , endy) = (self.dimension -1, self.dimension-1)
		max_fringe_len = 0
		fringe = [(0,(startx,starty, (-1, -1, 0)))];
		closedSet = [];
		while (len(fringe) != 0):
			if len(fringe)>max_fringe_len:
				max_fringe_len = len(fringe)

			(heuristicValue,(x, y, (parentx,parenty,pathLength))) = heapq.heappop(fringe);
			if (x,y) not in closedSet:
				if (x,y) == (endx,endy):
					break
				eligibleChildren = self.giveEligibleChild(x,y);
				for (cx,cy) in eligibleChildren:
					heuristic = distanceFunction((cx,cy),(endx,endy))+pathLength
					heapq.heappush(fringe,(heuristic,(cx,cy,(x,y,pathLength+1))))
				closedSet.append((x,y))
				
		return (max_fringe_len, len(closedSet))


p = [0.2, 0.3, 0.4, 0.5]
dim = 100
no_of_maze_per_prob = 20
'''
Fringe and closedSet parameters to compare both search algorithms.
'''
total_max_fringe1 = []
total_max_fringe2 = []
total_closedSet1 = []
total_closedSet2 = []

def cal():
	for i in range(no_of_maze_per_prob):
		mazeObject = Maze(dim, p)
		max_fringe_len1, closedSet1 = mazeObject.aStarSearch(helper.manhattanDistance)
		max_fringe_len2, closedSet2 = mazeObject.aStarSearch(helper.euclidDistance)
		
		total_max_fringe1.append(max_fringe_len1)
		total_max_fringe2.append(max_fringe_len2)
		total_closedSet1.append(closedSet1)
		total_closedSet2.append(closedSet2)
	
	plotGraph(total_max_fringe1, total_max_fringe2, total_closedSet1, total_closedSet2)

def plotGraph(total_max_fringe1, total_max_fringe2, total_closedSet1, total_closedSet2):
	fig, axs = plt.subplots(2)
	axs[0].plot(total_max_fringe1)
	axs[0].plot(total_max_fringe2)
	axs[0].title.set_text('Maximum length of fringe')
	axs[1].plot(total_closedSet1)
	axs[1].plot(total_closedSet2)
	axs[1].title.set_text('Length of Closed set')
	plt.show()

cal()
