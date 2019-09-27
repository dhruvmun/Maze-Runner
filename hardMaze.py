import maze
import helper
import random
import heapq

# This function returns the hardness values namely path length, explored nodes, max fringe length
# after running the astar algorithm on maze input with the given distanceFunction (defaults to manhattan distance)
def aStarWithDistanceFunction(maze, distanceFunction = helper.manhattanDistance):
	(startx, starty) = (0,0)
	(endx , endy) = (maze.dimension -1, maze.dimension-1)
	# path dictionary for tracing back the path after traversal
	path = {}
	# appending the initial element to priority queue starting co-ordinates, and parent co-ordinates
	# initial parent co-ordinates are (-1,-1) as a way to detect end of path while tracing back
	fringe = [(0,(startx,starty, (-1, -1, 0)))]

	maxFringeLength = 1
	closedSet = []
	# iterating until fringe length becomes zero
	while (len(fringe) != 0):
		fringeLength = len(fringe)
		if (maxFringeLength < fringeLength):
			# capturing latest max fringe length
			maxFringeLength = fringeLength
		# next best element to explore from fringe
		(heuristicValue,(x, y, (parentx,parenty,pathLength))) = heapq.heappop(fringe)
		if (x,y) not in closedSet:
			if (x,y) == (endx,endy):
				path[(x,y)] = (parentx,parenty)
				# once we reach the goal return with the required hardness values
				return (len(maze.getPath(path)),len(closedSet), maxFringeLength)
			eligibleChildren = maze.giveEligibleChild(x,y);
			for (cx,cy) in eligibleChildren:
				# calculating the heuristic value using distance function and adding pathLength
				heuristic = distanceFunction(cx,cy,endx,endy)+pathLength
				heapq.heappush(fringe,(heuristic,(cx,cy,(x,y,pathLength+1))))
			# once explored a node add it to closedSet 
			closedSet.append((x,y))
			# add parent of current explored node so that if it's actually in path it will help us to trace back
			path[(x,y)] = (parentx,parenty)
	return (0,len(closedSet),maxFringeLength)

# given all the hardness values returns only the explored nodes
def manhattanDistanceWithMaximalNodes(maze, pathLength, exploredNodes, maxFringeLength):
	# signum(pathLength) is used to see if maze is solvable or not
	# if maze is not solvable explored nodes doesn't make sense
	return signum(pathLength)*exploredNodes

# This function returns the hardness values namely path length, explored nodes, max fringe length
# after running the dfs algorithm on maze input
def dfsWithMaxFringe(maze, distanceFunction = None):
	(startx, starty) = (0,0)
	(endx , endy) = (maze.dimension -1, maze.dimension-1)
	# path dictionary for tracing back the path after traversal
	path = {};
	# appending the initial element to list starting co-ordinates, and parent co-ordinates
	# initial parent co-ordinates are (-1,-1) as a way to detect end of path while tracing back
	fringe = [(startx,starty, (-1,-1))];
	maxFringeLength = 1
	closedSet = [];
	# iterating until fringe length becomes zero
	while (len(fringe) != 0):
		fringeLength = len(fringe)
		if (maxFringeLength < fringeLength):
			maxFringeLength = fringeLength
		(x, y, (parentx,parenty)) = fringe.pop();
		if (x,y) not in closedSet:
			if (x,y) == (endx,endy):
				path[(x,y)] = (parentx,parenty)
				return (len(maze.getPath(path)), None, maxFringeLength);
			eligibleChildren = maze.giveEligibleChild(x,y);
			for (cx,cy) in eligibleChildren:
				fringe.append((cx,cy,(x,y)))
			closedSet.append((x,y))
			path[(x,y)] = (parentx,parenty)
	return (0, None, maxFringeLength);

# signum function
def signum(x):
	if x == 0:
		return 0
	elif (x > 0):
		return 1
	elif (x < 0):
		return -1

# given all the hardness values returns only the max fringe length
def dfsWithMaxFringeLength(maze, pathLength, exploredNodes, maxFringeLength):
	return signum(pathLength)*maxFringeLength

# used by genetic algorithm to give two mazes from two parent mazes
def getChild(maze1, maze2):
	childMaze1 = maze.Maze(maze1.dimension, 0)
	childMaze2 = maze.Maze(maze1.dimension, 0)
	for j in range(maze1.dimension):
		# first half columns are taken from maze1, maze2 for child1, child2
		if j < maze1.dimension/2:
			for i in range(maze1.dimension):
				childMaze1.mazeCells[i][j] = maze1.mazeCells[i][j]
				childMaze2.mazeCells[i][j] = maze2.mazeCells[i][j]
		# second half columns are taken from maze2, maze1 for child1, child2
		else:
			for i in range(maze1.dimension):
				childMaze1.mazeCells[i][j] = maze2.mazeCells[i][j]
				childMaze2.mazeCells[i][j] = maze1.mazeCells[i][j]
	return [childMaze1, childMaze2]

# randoming select dimension/2 number of cells to mutate else child transforms to a random child
# mutateProbability to decide whether to mutate a cell or not
# mutating is same as flipping the value
def mutateChild(childMaze, mutateProbability):
	for i in range(childMaze.dimension/2):
		if(random.uniform(0,1) < mutateProbability):
			row = random.randint(0,childMaze.dimension-1)
			column = random.randint(0,childMaze.dimension-1)
			childMaze.mazeCells[row][column] =  1 - childMaze.mazeCells[row][column]
	childMaze.mazeCells[0][0] = 0
	childMaze.mazeCells[childMaze.dimension-1][childMaze.dimension-1] = 0
	return childMaze

# generates initial population for beam search and gives a priority queue with hardness value as comparator
def generateInitialPopulation(dimension, probability, k, hardnessFunction, hardnessScore):
	population = []
	for i in range(k):
		# create a random maze and check for solvability, ie. path length
		currMaze = maze.Maze(dimension, probability)
		solvable = hardnessFunction(currMaze)
		# solvable[0] is path length
		while solvable[0] == 0:
			# generates a new maze if old is not solvable
			currMaze = maze.Maze(dimension, probability)
			solvable = hardnessFunction(currMaze)
		# pushes a solvable maze into priority queue by calculating hardness score
		heapq.heappush(population, (-hardnessScore(currMaze, solvable[0], solvable[1], solvable[2]),currMaze))
	return population

# breeds a new generation and takes k best population
def bestBreed(population, k, hardnessFunction, hardnessScore):
	newPopulation = []
	for i in range(k):
		for j in range(i,k):
			# generating child from two different parents
			childMazes = getChild(population[i][1], population[j][1])
			for childMaze in childMazes:
				# mutating child
				currMaze = mutateChild(childMaze, 0.5)
				hardness = hardnessFunction(currMaze)
				heapq.heappush(newPopulation, (-hardnessScore(currMaze, hardness[0], hardness[1], hardness[2]),currMaze))
	# returning best k population of the new generation
	return [heapq.heappop(newPopulation) for i in range(int(k))]

# implementation of beam search algorithm
# takes hardnessFunction and hardnessScore function 
def beamSearch(dimension, probability, k, hardnessFunction, hardnessScore):
	population = generateInitialPopulation(dimension, probability, k, hardnessFunction, hardnessScore)
	avgHardness = 0
	maxAvgHardness = 0
	# slackCount hardcoded to 2
	maxSlackCount = 2
	# toContinue tells whether to continue for next generation
	toContinue = True
	while toContinue: 
		population = bestBreed([heapq.heappop(population) for i in range(k)],k, hardnessFunction, hardnessScore)
		# calculating avgHardness of top k population
		avgHardness = -sum([i[0] for i in population])
		if avgHardness > maxAvgHardness :
			slackCount = 0
			toContinue = True
			maxAvgHardness = avgHardness
		else:
			# giving maxslackCount number of chances to breed even though avgHardness was not improved
			slackCount += 1
			if slackCount == maxSlackCount:
				toContinue = False
	# return top maze which is hardest along with hardness score
	return heapq.heappop(population)
