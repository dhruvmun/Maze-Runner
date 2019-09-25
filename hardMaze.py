import maze
import helper
import random
import heapq


def aStarWithDistanceFunction(maze, distanceFunction = helper.manhattanDistance):
	(startx, starty) = (0,0)
	(endx , endy) = (maze.dimension -1, maze.dimension-1)
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
				return (len(maze.getPath(path)),len(closedSet), maxFringeLength)
			eligibleChildren = maze.giveEligibleChild(x,y);
			for (cx,cy) in eligibleChildren:
				heuristic = distanceFunction(cx,cy,endx,endy)+pathLength
				heapq.heappush(fringe,(heuristic,(cx,cy,(x,y,pathLength+1))))
			closedSet.append((x,y))
			path[(x,y)] = (parentx,parenty)
	return (0,len(closedSet),maxFringeLength)

def manhattanDistanceWithMaximalNodes(maze, pathLength, exploredNodes, maxFringeLength):
	return signum(pathLength)*exploredNodes

def dfsWithMaxFringe(maze, distanceFunction = None):
	(startx, starty) = (0,0)
	(endx , endy) = (maze.dimension -1, maze.dimension-1)
	path = {};
	fringe = [(startx,starty, (-1,-1))];
	maxFringeLength = 1
	closedSet = [];
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

def signum(x):
	if x == 0:
		return 0
	elif (x > 0):
		return 1
	elif (x < 0):
		return -1

def dfsWithMaxFringeLength(maze, pathLength, exploredNodes, maxFringeLength):
	return signum(pathLength)*maxFringeLength

def getChild(maze1, maze2):
	childMaze1 = maze.Maze(maze1.dimension, 0)
	childMaze2 = maze.Maze(maze1.dimension, 0)
	for j in range(maze1.dimension):
		if j < maze1.dimension/2:
			for i in range(maze1.dimension):
				childMaze1.mazeCells[i][j] = maze1.mazeCells[i][j]
				childMaze2.mazeCells[i][j] = maze2.mazeCells[i][j]
		else:
			for i in range(maze1.dimension):
				childMaze1.mazeCells[i][j] = maze2.mazeCells[i][j]
				childMaze2.mazeCells[i][j] = maze1.mazeCells[i][j]
	return [childMaze1, childMaze2]

def mutateChild(childMaze, mutateProbability):
	for i in range(childMaze.dimension/2):
		if(random.uniform(0,1) < mutateProbability):
			row = random.randint(0,childMaze.dimension-1)
			column = random.randint(0,childMaze.dimension-1)
			childMaze.mazeCells[row][column] =  1 - childMaze.mazeCells[row][column]
	childMaze.mazeCells[0][0] = 0
	childMaze.mazeCells[childMaze.dimension-1][childMaze.dimension-1] = 0
	return childMaze

def generateInitialPopulation(dimension, probability, k, hardnessFunction, hardnessScore):
	population = []
	for i in range(k):
		currMaze = maze.Maze(dimension, probability)
		solvable = hardnessFunction(currMaze)
		while solvable[0] == 0:
			currMaze = maze.Maze(dimension, probability)
			solvable = hardnessFunction(currMaze)
		heapq.heappush(population, (-hardnessScore(currMaze, solvable[0], solvable[1], solvable[2]),currMaze))
	return population

def bestBreed(population, k, hardnessFunction, hardnessScore):
	newPopulation = []
	for i in range(k):
		for j in range(i,k):
			childMazes = getChild(population[i][1], population[j][1])
			for childMaze in childMazes:
				currMaze = mutateChild(childMaze, 0.5)
				hardness = hardnessFunction(currMaze)
				heapq.heappush(newPopulation, (-hardnessScore(currMaze, hardness[0], hardness[1], hardness[2]),currMaze))
	return [heapq.heappop(newPopulation) for i in range(int(k))]

def beamSearch(dimension, probability, k, hardnessFunction, hardnessScore):
	population = generateInitialPopulation(dimension, probability, k, hardnessFunction, hardnessScore)
	avgHardness = 0
	maxAvgHardness = 0
	maxSlackCount = 2
	toContinue = True
	while toContinue: 
		population = bestBreed([heapq.heappop(population) for i in range(k)],k, hardnessFunction, hardnessScore)
		avgHardness = -sum([i[0] for i in population])
		if avgHardness > maxAvgHardness :
			slackCount = 0
			toContinue = True
			maxAvgHardness = avgHardness
		else:
			slackCount += 1
			if slackCount == maxSlackCount:
				toContinue = False
	return heapq.heappop(population)
