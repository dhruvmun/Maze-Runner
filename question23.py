import maze
import helper
import matplotlib.pyplot as plt

prob = [0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]
dim = 100

solvability = []
no_of_maze_per_prob = 50

def probability_threshold():
	for p in  prob:
		unsol = 0
		for i in range(no_of_maze_per_prob):
			mazeObject = maze.Maze(dim, p)
			path = mazeObject.aStarSearch(helper.manhattanDistance)
			if path == []:
				unsol += 1

		if unsol != no_of_maze_per_prob:
			p0 = p

		solvability.append((1-(unsol/no_of_maze_per_prob)))
	return p0

def plotgraph():
	plt.plot(prob, solvability)
	plt.ylabel('Solvability')
	plt.xlabel('Density')
	plt.title('Density vs Solvability')
	plt.show()

probability_threshold()
plotgraph()
