import maze
import helper
import heapq
import matplotlib.pyplot as plt
import random

def giveFireChild(x, y, q, k):
	fireProb = 1-pow((1-q),k)
	if (random.uniform(0, 1) <= fireProb):
		return True
	else:
		return False


def expandFire(mazeObject, fireset, q):
	for i in range(mazeObject.dimension):
		for j in range(mazeObject.dimension):
			if(mazeObject.mazeCells[i][j] == 0):
				k = mazeObject.giveFireNeighbours(i,j)
				if(k==0):
					continue
				else:
					if(giveFireChild(i, j, q, k)):
						fireset.append((i,j))
						mazeObject.mazeCells[i][j] = 2
	return (fireset, mazeObject)

def aStarSearch(mazeObject, distanceFunction, startx,starty, endx , endy):
	path = {}
	fringe = [(0,(startx,starty, (-1, -1, 0)))]
	closedSet = []
	while (len(fringe) != 0):
		(heuristicValue,(x, y, (parentx,parenty,pathLength))) = heapq.heappop(fringe)
		if (x,y) not in closedSet:
			if (x,y) == (endx,endy):
				path[(x,y)] = (parentx,parenty)
				return mazeObject.getPath(path, endx, endy)
			eligibleChildren = mazeObject.giveEligibleChild(x,y);
			for (cx,cy) in eligibleChildren:
				heuristic = distanceFunction(cx,cy,endx,endy)+pathLength
				heapq.heappush(fringe,(heuristic,(cx,cy,(x,y,pathLength+1))))
			closedSet.append((x,y))
			path[(x,y)] = (parentx,parenty)
	return []

def findPath(p,q):
	# 0->Open, 1->Block, 2->fire
	shortestPath_fire = []
	shortestPath = []
	while (shortestPath_fire == [] or shortestPath == []):
		mazeObject = maze.Maze(dim, p)
		shortestPath_fire = aStarSearch(mazeObject, helper.manhattanDistance, 0,dim-1, dim-1,0)
		shortestPath = aStarSearch(mazeObject, helper.manhattanDistance, 0,0, dim-1,dim-1)

	mazeObject.mazeCells[0][dim-1] = 2
	fireset = [(0,dim-1)]

	while shortestPath != []:
		next_step = shortestPath.pop(0)
		(fireset, mazeObject) = expandFire(mazeObject, fireset, q)
		# print fireset
		# for row in mazeObject.mazeCells:
		# 	print row
		# print next_step
		if next_step in fireset:
			return 0  #"Dead"
	return 1  #"Success"

def plotgraph():
	plt.plot(qs, avgsuccess)
	plt.xlabel('flamability')
	plt.ylabel('avg Success')
	plt.title('flamability vs success')
	plt.show()


# p0 = 0.3
# dim = 10
# qs = []
# for i in range(11):
# 	qs.append(float(i)/10)
# no_of_maze_per_q = 50
# avgsuccess = []
# for q in qs:
# 	d=0
# 	s=0
# 	for i in range(no_of_maze_per_q):
# 		a = findPath(0.2,q)
# 		# print ("q: "+str(q) + " i: " + str(i) + " a: "+ str(a))
# 		if a==0:
# 			d+=1
# 		elif a==1:
# 			s+=1
# 	print ("<<<<<<<<<<<<< "+ str(s) + "/" + str(s+d))
# 	avgsuccess.append(float(s)/(s+d))
#
# # x = raw_input()
# plotgraph()

