import random
import heapq
import helper

class Maze:
	'''
	parameters: int dim- dimension;
				float p- probability;
				list mazeCells;
	Returns the mazeObject for a given value of dim and p
	'''
	def __init__(self, dim, p):
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

		
	def BFS(self):
		'''
		Takes as input the Maze maze Object and
		returns the path traversed according to Breadth First Search
		Fringe stores the values as tuple of (x,y,parent) x and y are coordinates of current state
		fringe DataStructure: Queue
		'''
		fringe = [(0, 0,(-1,-1))]
		goal_state = (self.dimension-1,self.dimension-1)
		closedSet = []
		path = {}
		while len(fringe) != 0:		
			(x,y,(parentx, parenty)) = fringe.pop(0)
			'''
			For each x and y we check they aren't alread visited i.e. not in closed set
			and generate the eligible child and append them to the fringe.
			Also add to the path dictonary the key:current state and value: parent state pair  
			Add the current state (x,y) to the closed set.
			'''
			if (x,y) not in closedSet:
				childList = self.giveEligibleChild(x,y)		
				path[(x,y)] = (parentx,parenty)
				for (childx, childy) in childList:
					fringe.append((childx, childy, (x,y)))
					if (childx, childy) == goal_state:  
						path[(childx,childy)] = (x,y)
						return self.getPath(path, childx, childy)
				closedSet.append((x,y))
		return []

	def treeSearch(self):
		'''
		Similar Implementation to DFS used for A* search algorithm.
		'''
		(startx, starty) = (0,0)
		(endx , endy) = (self.dimension -1, self.dimension-1)
		path = {};
		fringe = [(startx,starty, (-1,-1))];
		closedSet = [];
		while (len(fringe) != 0):
			(x, y, (parentx,parenty)) = fringe.pop();
			if (x,y) not in closedSet:
				if (x,y) == (endx,endy):
					path[(x,y)] = (parentx,parenty)
					return (self.getPath(path, endx, endy), closedSet);
				eligibleChildren = self.giveEligibleChild(x,y);
				for (cx,cy) in eligibleChildren:
					fringe.append((cx,cy,(x,y)))
				closedSet.append((x,y))
				path[(x,y)] = (parentx,parenty)
		return ([], closedSet);

	def bidirection(self):
		'''
		A bidirectional BFS implementation
		input: Maze Object
		return: path
		fringe1, closed1: from Source
		fringe2, closed2: from Goal
		fringe DataStructure: Queue
		'''
		fringe1 = [[(0, 0)]]	#inital source state
		fringe2 = [[(self.dimension - 1, self.dimension - 1)]]	#Goal state
		closed1 = {(0, 0): True} 
		closed2 = {(self.dimension - 1, self.dimension - 1): True}
		while fringe1 and fringe2:
			if fringe1:
				'''
				BFS implementation from source
				'''
				recent_path1 = fringe1.pop(0)
				(x, y) = recent_path1[-1]
				children = self.giveEligibleChild(x, y)
				for child in children:
					if child not in closed1:
						closed1[child] = True
						new_Path = list(recent_path1)  # New list to append in fringe after adding the child
						new_Path.append(child)
						fringe1.append(new_Path)
						'''
						child reaches the goal or intersects with the fringe from goal
						'''
						if child == (self.dimension - 1, self.dimension - 1) or child in fringe2:
							return new_Path
			if fringe2:
				'''
				BFS implementation from Goal
				'''
				recent_path2 = fringe2.pop(0)
				(x, y) = recent_path2[-1]
				children = self.giveEligibleChild(x, y)
				for child in children:
					if child not in closed2:
						closed2[child] = True
						new_Path = list(recent_path2)  # New list to append in fringe after adding the child
						new_Path.append(child)
						fringe2.append(new_Path)
						'''
						child reaches the goal or intersects with the fringe from goal
						'''
						if child == (0, 0) or child in fringe1:
							return new_Path
		return []

	def dfs(self):
		'''
		Takes as input the Maze maze Object and
		returns the path traversed according to Breadth First Search
		Fringe stores the values as tuple of (x,y,parent) x and y are coordinates of current state
		fringe DataStructure: Stack
		'''
		goal_state = (self.dimension-1,self.dimension-1)
		fringe = [(0,0,(-1,-1))] #x,y,path
		closed_set = [] 
		path = {}
		while (len(fringe)):
			(x,y,(parentx, parenty)) = fringe.pop()
			current_state = (x,y)
			'''
			For each x and y we check they aren't alread visited i.e. not in closed set
			and generate the eligible child and append them to the fringe.
			Also add to the path dictonary the key:current state and value: parent state pair  
			Add the current state (x,y) to the closed set.
			'''
			if(current_state not in closed_set):
				if (current_state == goal_state):
					path[current_state] = (parentx, parenty)
					return self.getPath(path, goal_state[0], goal_state[1])
				
				children = self.giveEligibleChild(x,y)
				for a,b in children:
					fringe.append((a,b,(x,y)))

				path[current_state] = (parentx, parenty)
				closed_set.append(current_state)
		return []


	def aStarSearch(self, distanceFunction):
		'''
		parameters: mazeObject and distanceFunction- Manhatan or Euclid
		return: path
		fringe: priority, tuple of(x,y,parent)
		fringe DataStructure: PriorityQueue/Heap
		'''
		(startx, starty) = (0,0)
		(endx , endy) = (self.dimension -1, self.dimension-1)
		path = {}
		fringe = [(0,(startx,starty, (-1, -1, 0)))]
		closedSet = [];
		while (len(fringe) != 0):
			(heuristicValue,(x, y, (parentx,parenty,pathLength))) = heapq.heappop(fringe);
			if (x,y) not in closedSet:
				if (x,y) == (endx,endy):
					path[(x,y)] = (parentx,parenty)
					return self.getPath(path, endx, endy)
				eligibleChildren = self.giveEligibleChild(x,y);
				for (cx,cy) in eligibleChildren:
					heuristic = distanceFunction(cx,cy,endx,endy)+pathLength
					heapq.heappush(fringe,(heuristic,(cx,cy,(x,y,pathLength+1))))
				closedSet.append((x,y))
				path[(x,y)] = (parentx,parenty)
		return [];


	def getPath(self, path, endx, endy):
		'''
		returns path by backtracking the parent of current_state recurssively
		'''
		pathList = [(endx, endy)]
		while path[pathList[-1]]!=(-1,-1):
			pathList.append(path[pathList[-1]])
		pathList.reverse()
		return pathList

	# Gives hardness values defined in the problem by running astar algorithm with given distanceFunction
	# path length, explored nodes, max fringe length
	def hardnessValues(self, distanceFunction):
		(startx, starty) = (0,0)
		(endx , endy) = (self.dimension -1, self.dimension-1)
		path = {}
		fringe = [(0,(startx,starty, (-1, -1, 0)))]
		maxFringeLength = 1
		closedSet = []
		while (len(fringe) != 0):
			fringeLength = len(fringe)
			if (maxFringeLength < fringeLength):
				maxFringeLength = fringeLength
			(heuristicValue,(x, y, (parentx,parenty,pathLength))) = heapq.heappop(fringe)
			if (x,y) not in closedSet:
				if (x,y) == (endx,endy):
					path[(x,y)] = (parentx,parenty)
					return (len(self.getPath(path, endx, endy)),len(closedSet), maxFringeLength)
				eligibleChildren = self.giveEligibleChild(x,y);
				for (cx,cy) in eligibleChildren:
					heuristic = distanceFunction(cx,cy,endx,endy)+pathLength
					heapq.heappush(fringe,(heuristic,(cx,cy,(x,y,pathLength+1))))
				closedSet.append((x,y))
				path[(x,y)] = (parentx,parenty)
		return (0,len(closedSet),maxFringeLength)

	# Given the hardness values above calculating a hardness score from them giving particular weights
	def hardnessScore(self, pathLength, exploredNodes, maxFringeLength):
		# normalize the above hardness values using dimension of the maze
		if pathLength != 0 :
			pathScore = float(2*self.dimension-1)/float(pathLength)
		else:
			return 0
		exploredScore = exploredNodes/float(self.dimension*self.dimension)
		fringeScore = maxFringeLength/float(self.dimension*self.dimension)
		return (2*pathScore + 3*exploredScore + fringeScore)/6

	# gives the count of neigbours which has fire
	def giveFireNeighbours(self, x, y):
		k = 0
		if(x-1>=0 and self.mazeCells[x-1][y]==2):	#Blocked cell cannot catch fire
			k+=1
		if(x+1<=self.dimension-1 and self.mazeCells[x+1][y]==2):
			k+=1
		if(y-1>=0 and self.mazeCells[x][y-1]==2):
			k+=1
		if(y+1<=self.dimension-1 and self.mazeCells[x][y+1]==2):
			k+=1
		return k

	# gives the list of neighbours unblocked and not already visited in closed set
	def giveUnclosedChild(self, x, y,closed):
		children=[]
		reqChild=[]
		backChild=[]
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
		# if len(children)==1:
		# 	return children
		# else:
		for child in children:
			if child not in closed:
				reqChild.append(child)
			else:
				backChild.append(child)
		if len(reqChild)==0:
			return backChild
		else:
			return reqChild