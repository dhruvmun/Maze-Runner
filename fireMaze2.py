import maze
import helper
import random

def giveFireChild(mazeObject, fireset, x, y, q, k):
	fireProb = 1-pow((1-q),k)
	if (fireProb>=random.uniform(0, 1)):
		mazeObject.mazeCells[x][y]=2
		fireset.append((x,y))


def expandFire(mazeObject, fireset, q):
	for i in range(mazeObject.dimension):
		for j in range(mazeObject.dimension):
			if(mazeObject.mazeCells[i][j] == 0):
				k = mazeObject.giveFireNeighbours(i,j)
				if(k==0):
					continue
				else
					giveFireChild(mazeObject, fireset, i, j, q, k)
		

def findPath():
	# 0->Open, 1->Block, 2->fire
	# mazeObject = maze.Maze(dim, p)

	# shortestPath = mazeObject.aStarSearch(helper.euclidDistance)
	# if shortestPath == []:
	# 	return "No Path Exist"
	# while shortestPath != []:
	# 	next_step = shortestPath.pop(0)
	Fire(m1, fireset, 0.2)
		# if next_step in fireset:
		# 	return "Dead"
	# return "Success"



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
def minimax(child,player):
	(x,y)=child
	if child==m1.mazeCells[m1.dimension-1][m1.dimension-1]:
		print("Success")
		return False if player else True

	if player:
		# value=100
		children=m1.giveEligibleChild(x,y)
		print("Children")
		print(children)
		for child in children:
			if child not in fringe:
				(a,b)=child
				closed.append(child)
				listObject.append(heuristic(a,b))
		max1=listObject.index(max(listObject))
		print(listObject,max1)
		if max1+1:
			p,q=children[max1]
			fringe.append((p,q))
			print("List")
			print(listObject)
			minimax((p, q), False)
			listObject.clear()


	else:
		if (e,y)==(m1.dimension-1,0):
			print("Dead")
			return False
		else:
			findPath()
			minimax(child,True)

p = 0.2
dim = 20
# a = findPath(0.2,0.2)
# print (a)
m1=maze.Maze(dim,p)
m1.mazeCells[0][dim-1] = 2
fireset = [(0,dim-1)]
# goal=[]
(x,y)=(0,0)
(e,f)=(0,m1.dimension-1)
print(minimax((x,y),True))
