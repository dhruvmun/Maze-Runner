import maze
import helper
import time
import visualization

# runs each algorithm for the below parameters and prints time taken
dimension = 50
probability = 0.2
path = []
# creates a maze until it is solvable
while len(path) == 0:
	mazeObject = maze.Maze(dimension,probability)
	path = mazeObject.aStarSearch(helper.manhattanDistance)
print ("Dimension : " + str(dimension) + " Probability : " + str(probability))

# calculates the time taken for the algorithm to run
startTime = time.time()
dfsPath = mazeObject.dfs()
endTime = time.time()
print ("DFS time: " + str(endTime-startTime) + "sec Length : " + str(len(dfsPath)))

# Using visualise class to visualise the path and the maze generated
visualise = visualization.Visualize("DFS", 'yellow')
visualise.drawMaze(mazeObject)
visualise.drawPath(dfsPath)
visualise.exportPng('DFS22')
visualise.clearScreen()

startTime = time.time()
bfsPath = mazeObject.BFS()
endTime = time.time()
print ("BFS time: " + str(endTime-startTime) + "sec Length : " + str(len(bfsPath)))

visualise = visualization.Visualize("BFS", 'green')
visualise.drawMaze(mazeObject)
visualise.drawPath(bfsPath)
visualise.exportPng('BFS22')
visualise.clearScreen()

startTime = time.time()
euclidPath = mazeObject.aStarSearch(helper.euclidDistance)
endTime = time.time()
print ("Euclid A* time: " + str(endTime-startTime) + "sec Length : " + str(len(euclidPath)))

visualise = visualization.Visualize("Euclid A*", 'red')
visualise.drawMaze(mazeObject)
visualise.drawPath(euclidPath)
visualise.exportPng('EuclidA22')
visualise.clearScreen()

startTime = time.time()
manhattanPath = mazeObject.aStarSearch(helper.manhattanDistance)
endTime = time.time()
print ("Manhattan A* time: " + str(endTime-startTime) + "sec Length : " + str(len(manhattanPath)))

visualise = visualization.Visualize("Manhattan A*", 'blue')
visualise.drawMaze(mazeObject)
visualise.drawPath(manhattanPath)
visualise.exportPng('ManhattanA22')
visualise.clearScreen()