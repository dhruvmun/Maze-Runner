import maze
import helper
import time

# iterations: number of iterations for each dimension, probability
# timeLimit: choosen time limit till which dimension should be increased
# dimension, probability
# function calculates average time taken for dimension and probability
def avgTime(iterations, timeLimit, dimension, probability):
	timeTaken = 0
	while timeTaken <= timeLimit:
		timeTaken = 0
		for i in range(iterations):
			path = []
			while path == []:
				mazeObject = maze.Maze(dimension, probability)
				path =  mazeObject.aStarSearch(helper.manhattanDistance)
			startTime = time.time()
			path =  mazeObject.aStarSearch(helper.manhattanDistance)
			endTime = time.time()
			timeTaken += endTime - startTime
			print (str(dimension) + "," + str(probability) + " , " + str(timeTaken) + "," + str(len(path)))
		timeTaken /= iterations
		print ("Average time ," + str(dimension) + "," + str(probability) + " , " + str(timeTaken))
		dimension += 10

dimension = 100
iterations = 3
timeLimit = 60
bins = [0.2]
for probability in bins:
	# probability = (prob+1)/10.0
	avgTime(iterations, timeLimit, dimension, probability)
	
		


