import maze
import helper
import random
import heapq

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

def generateInitialPopulation(dimension, probability, k):
	population = []
	for i in range(k):
		currMaze = maze.Maze(dimension, probability)
		solvable = currMaze.hardnessValues(helper.manhattanDistance)
		while solvable[0] == 0:
			currMaze = maze.Maze(dimension, probability)
			solvable = currMaze.hardnessValues(helper.manhattanDistance)
		heapq.heappush(population, (-currMaze.hardnessScore(solvable[0],solvable[1],solvable[2]),currMaze))
	return population

def bestBreed(population, k):
	newPopulation = []
	for i in range(k):
		for j in range(i,k):
			childMazes = getChild(population[i][1], population[j][1])
			for childMaze in childMazes:
				currMaze = mutateChild(childMaze, 0.5)
				hardness = currMaze.hardnessValues(helper.manhattanDistance)
				heapq.heappush(newPopulation, (-currMaze.hardnessScore(hardness[0],hardness[1],hardness[2]),currMaze))
	return [heapq.heappop(newPopulation) for i in range(int(k))]

def beamSearch(dimension, probability, k):
	population = generateInitialPopulation(dimension, probability, k)
	avgHardness = 0
	maxAvgHardness = 0
	maxSlackCount = 2
	toContinue = True
	while toContinue: 
		population = bestBreed([heapq.heappop(population) for i in range(k)],k)
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
