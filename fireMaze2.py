import maze
import helper
import random
import fireMaze

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


def heuristic(a,b):
		x=a
		y=b
		k = 0
		if (x - 1 >= 0 and m1.mazeCells[x - 1][y] == 0):  # Blocked cell cannot catch fire
			k += 1
		if (x + 1 <= dim - 1 and m1.mazeCells[x + 1][y] == 0):
			k += 1
		if (y - 1 >= 0 and m1.mazeCells[x][y - 1] == 0):
			k += 1
		if (y + 1 <= dim - 1 and m1.mazeCells[x][y + 1] == 0):
			k += 1
		return k
		# fireProb = 1 - pow((1 - q), k)
		# if (fireProb >= p0):
		# 	mazeObject.mazeCells[x][y] = 2
		# 	fireset.append((x, y))
fringe=[(0,0)]
listObject=[]
closed=[]
def minmax(m1, child,player,fireset):
	if child==m1.mazeCells[m1.dimension-1][m1.dimension-1]:
		print("Goal State reached by Man")
		return True

	if player:
		while fringe:
			(x,y)=fringe.pop()
			if (x,y) not in closed and (x,y) not in fireset:
				if (x,y)==(m1.dimension-1,m1.dimension-1):
					return True
				children=m1.giveEligibleChild(x,y)
				print("Children")
				print(children)
				listObject.clear()
				for child in children:
					(a,b)=child
					listObject.append(heuristic(a,b))
				closed.append((x,y))
				max1=listObject.index(max(listObject))
				print(listObject,max1)
				if max1+1:
					p,q=children[max1]
					fringe.append((p,q))
					# print("List")
					# print(listObject)
					minmax(m1, (p, q), False,fireset)



	else:
		(fireset,m1)=expandFire(m1,fireset, 0.2)
		print("Fire")
		print(fireset)
		if fireset[-1]==child or fireset[-1]==m1.mazeCells[m1.dimension - 1][m1.dimension - 1]:
				Print("Dead")
				return False
		else:
			minmax(m1,child,True,fireset)

def generateFireMaze(dim, p):
	shortestPath_fire = []
	shortestPath = []
	while (shortestPath_fire == [] or shortestPath == []):
		mazeObject = maze.Maze(dim, p)
		shortestPath_fire = fireMaze.aStarSearch(mazeObject, helper.manhattanDistance, 0, dim - 1, dim - 1, 0)
		shortestPath = fireMaze.aStarSearch(mazeObject, helper.manhattanDistance, 0, 0, dim - 1, dim - 1)

	mazeObject.mazeCells[0][dim - 1] = 2
	fireset = [(0, dim - 1)]
	return (fireset, mazeObject)

p = 0.3
dim = 5

(fireset,m1) = generateFireMaze(dim,p)
# goal=[]
(x,y)=(0,0)
# (e,f)=(0,m1.dimension-1)
for i in range(m1.dimension-1):
	print(m1.mazeCells[i])
print(minmax(m1,(x,y),True,fireset))
