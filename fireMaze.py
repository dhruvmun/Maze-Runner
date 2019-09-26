import maze
import helper
import heapq
import matplotlib.pyplot as plt

def giveFireChild(mazeObject, fireset, x, y, q, p0):
	k = 0
	if(x-1>=0 and mazeObject.mazeCells[x-1][y]==2):	#Blocked cell cannot catch fire
		k+=1
	if(x+1<=dim-1 and mazeObject.mazeCells[x+1][y]==2):
		k+=1
	if(y-1>=0 and mazeObject.mazeCells[x][y-1]==2):
		k+=1
	if(y+1<=dim-1 and mazeObject.mazeCells[x][y+1]==2):
		k+=1
	fireProb = 1-pow((1-q),k)
	if(fireProb>=p0):
		mazeObject.mazeCells[x][y]=2
		fireset.append((x,y))

def Fire(mazeObject, fireset, q):
	l = len(fireset)
	for i in range(l):
		(x,y) = fireset[i]
		if(x-1>=0 and mazeObject.mazeCells[x-1][y]==0):	#Blocked cell cannot catch fire
			giveFireChild(mazeObject, fireset,x-1,y,q,p0)
		if(x+1<=dim-1 and mazeObject.mazeCells[x+1][y]==0):
			giveFireChild(mazeObject, fireset,x+1,y,q,p0)
		if(y-1>=0 and mazeObject.mazeCells[x][y-1]==0):
			giveFireChild(mazeObject, fireset,x,y-1,q,p0)
		if(y+1<=dim-1 and mazeObject.mazeCells[x][y+1]==0):
			giveFireChild(mazeObject, fireset,x,y+1,q,p0)

def aStarSearch(mazeObject, distanceFunction, (startx,starty), (endx , endy)):
	path = {}
	fringe = [(0,(startx,starty, (-1, -1, 0)))]
	closedSet = []
	while (len(fringe) != 0):
		(heuristicValue,(x, y, (parentx,parenty,pathLength))) = heapq.heappop(fringe)
		if (x,y) not in closedSet:
			if (x,y) == (endx,endy):
				path[(x,y)] = (parentx,parenty)
				return mazeObject.getPath(path)
			eligibleChildren = mazeObject.giveEligibleChild(x,y);
			for (cx,cy) in eligibleChildren:
				heuristic = distanceFunction(cx,cy,endx,endy)+pathLength
				heapq.heappush(fringe,(heuristic,(cx,cy,(x,y,pathLength+1))))
			closedSet.append((x,y))
			path[(x,y)] = (parentx,parenty)
	return []

def findPath(p, q):
	# 0->Open, 1->Block, 2->fire
	mazeObject = maze.Maze(dim, p)
	mazeObject.mazeCells[0][dim-1] = 2
	fireset = [(0,dim-1)]

	shortestPath = aStarSearch(mazeObject, helper.euclidDistance, (0,0), (dim-1,dim-1))
	shortestPath_fire = []
	while shortestPath_fire != []:
		shortestPath_fire = aStarSearch(mazeObject, helper.euclidDistance, (0,dim-1), (dim-1,0))
	
	if shortestPath == []:
		return -1  #"No Path Exist"
	while shortestPath != []:
		next_step = shortestPath.pop(0)
		Fire(mazeObject, fireset, q)
		if next_step in fireset:
			return 0  #"Dead"
	return 1  #"Success"

def plotgraph():
	plt.plot(qs, avgsuccess)
	plt.xlabel('flamability')
	plt.ylabel('avg Success')
	plt.title('flamability vs success')
	plt.show()


p0 = 0.3
dim = 100
qs = [0.0,0.1,0.2,0.3,0.4,0.5]
no_of_maze_per_q = 10
avgsuccess = []
for q in qs:
	d=0
	s=0
	for i in range(no_of_maze_per_q):	
		a = findPath(0.2,q)
		if a==0:
			d+=1
		elif a==1:
			s+=1
	avgsuccess.append(float(s/(s+d)))

plotgraph()
