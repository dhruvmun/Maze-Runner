import maze
import helper
import time

dimension = 200
probability = 0.2
path = []
while len(path) == 0:
	mazeObject = maze.Maze(dimension,probability)
	path = mazeObject.aStarSearch(helper.manhattanDistance)
print "Dimension : " + str(dimension) + " Probability : " + str(probability)

startTime = time.time()
dfsPath = mazeObject.dfs()
dfsPath2 = mazeObject.treeSearch()
print dfsPath == dfsPath2
endTime = time.time()
print "DFS time: " + str(endTime-startTime) + "sec Length : " + str(len(dfsPath))

startTime = time.time()
bfsPath = mazeObject.BFS()
endTime = time.time()
print "BFS time: " + str(endTime-startTime) + "sec Length : " + str(len(bfsPath))
		
startTime = time.time()
euclidPath = mazeObject.aStarSearch(helper.euclidDistance)
endTime = time.time()
print "Euclid A* time: " + str(endTime-startTime) + "sec Length : " + str(len(euclidPath))

startTime = time.time()
manhattanPath = mazeObject.aStarSearch(helper.manhattanDistance)
endTime = time.time()
print "Manhattan A* time: " + str(endTime-startTime) + "sec Length : " + str(len(manhattanPath))