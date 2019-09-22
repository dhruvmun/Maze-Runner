import maze
import helper
import time

def avgTime(iterations, timeLimit, dimension, probability):
	timeTaken = 0
	while timeTaken <= timeLimit:
		timeTaken = 0
		for i in range(iterations):
			startTime = time.time()
			mazeObject = maze.Maze(dimension, probability)
			path =  mazeObject.aStarSearch(helper.euclidDistance)
			endTime = time.time()
			timeTaken += endTime - startTime
			print str(dimension) + "," + str(probability) + " , " + str(timeTaken) + "," + str(len(path))
		timeTaken /= iterations
		print "Average time : " + str(dimension) + "," + str(probability) + " , " + str(timeTaken)
		dimension += 10

dimension = 100
iterations = 3
timeLimit = 60
bins = 9
for prob in range(bins):
	probability = (prob+1)/10.0
	avgTime(iterations, timeLimit, dimension, probability)
	
		


