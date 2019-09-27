import maze
import helper
import matplotlib.pyplot as plt

prob = [0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5] #Range of probability for which we will be checking the solvability
dim = 50

solvability = []
no_of_maze_per_prob = 100

def probability_threshold():
	'''
	Function to calculate the probability threshold for a range of values of probability
	'''
	for p in  prob:
		unsol = 0
		for i in range(no_of_maze_per_prob):
			mazeObject = maze.Maze(dim, p)
			path = mazeObject.aStarSearch(helper.manhattanDistance) #Returns the shortest path from source to Goal
			if path == []: #That is no solution exists
				unsol += 1
			# print (str(p)+": "+ str(unsol))
		if unsol != no_of_maze_per_prob:
			p0 = p

		solvability.append((1-(float(unsol)/no_of_maze_per_prob)))
	return p0

def plotgraph():
	"""
	A function to plot the graph between probability and solvability
	"""
	plt.plot(prob, solvability)
	plt.ylabel('Solvability')
	plt.xlabel('Density')
	plt.title('Density vs Solvability')
	plt.show()

probability_threshold()
plotgraph()
