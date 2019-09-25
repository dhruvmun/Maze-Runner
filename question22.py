import maze
import helper
import time
import visualization

dimension = 15
probability = 0.2
path = []
while len(path) == 0:
	mazeObject = maze.Maze(dimension,probability)
	path = mazeObject.aStarSearch(helper.manhattanDistance)
print "Dimension : " + str(dimension) + " Probability : " + str(probability)

startTime = time.time()
dfsPath = mazeObject.dfs()
endTime = time.time()
print "DFS time: " + str(endTime-startTime) + "sec Length : " + str(len(dfsPath))

visualise = visualization.Visualize("DFS", 'yellow')
visualise.drawMaze(mazeObject)
visualise.drawPath(dfsPath)

startTime = time.time()
bfsPath = mazeObject.BFS()
endTime = time.time()
print "BFS time: " + str(endTime-startTime) + "sec Length : " + str(len(bfsPath))

visualise = visualization.Visualize("BFS", 'green')
# visualise.drawMaze(mazeObject)
visualise.drawPath(bfsPath)

startTime = time.time()
euclidPath = mazeObject.aStarSearch(helper.euclidDistance)
endTime = time.time()
print "Euclid A* time: " + str(endTime-startTime) + "sec Length : " + str(len(euclidPath))

visualise = visualization.Visualize("Euclid A*", 'red')
# visualise.drawMaze(mazeObject)
visualise.drawPath(euclidPath)

startTime = time.time()
manhattanPath = mazeObject.aStarSearch(helper.manhattanDistance)
endTime = time.time()
print "Manhattan A* time: " + str(endTime-startTime) + "sec Length : " + str(len(manhattanPath))

visualise = visualization.Visualize("Manhattan A*", 'blue')
# visualise.drawMaze(mazeObject)
visualise.drawPath(manhattanPath)