import maze
import helper
import random
import fireMaze

def giveFireChild(q, k):
	fireProb = 1-pow((1-q),k)
	if (random.uniform(0, 1) <= fireProb):		#If random number generated comes less than fireprobability, fire will spread.
		return True
	else:
		return False


def expandFire(mazeObject, fireset, q):
	oldMazeObject = mazeObject			#Use previous mazeobject to get information about previously updated fire cell
	mazeObject = maze.Maze(oldMazeObject.dimension, oldMazeObject.probability)
	for i in range(mazeObject.dimension):
		for j in range(mazeObject.dimension):
			mazeObject.mazeCells[i][j] = oldMazeObject.mazeCells[i][j]	#To get states of fire from Last Maze
			if(mazeObject.mazeCells[i][j] == 0):
				k = oldMazeObject.giveFireNeighbours(i,j)	#Considering previous values find new Fire neighbours
				if(k==0):
					continue
				else:
					if(giveFireChild(q, k)):
						fireset.append((i,j))
						mazeObject.mazeCells[i][j] = 2
	return (fireset, mazeObject)

#Function to calculate best neighbouring cell to visit
# For each neighbour of child total neighbours which are unblocked( not in fire and not blocked)
# are calculated and that decides our best next state to move.
# For each neighbour a K value is returned which tells us how many of it's neighbours can be visited.
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

fringe=[(0,0)]
listObject=[]	#List to store k values for each child
closed=[]		#Closed State to store visited nodes
#  Player is a boolean value if True then Player moves and if False then Fire Part is executed
def minmax(m1, child,player,fireset):
	if child==m1.mazeCells[m1.dimension-1][m1.dimension-1]:
		print("Goal State reached by Man")
		return True

	if player:
		while fringe:
			(x,y)=fringe.pop()
			if (x,y)==(m1.dimension-1,m1.dimension-1):
				return True
			children=m1.giveUnclosedChild(x,y,closed)	#Gives eligible child which is not in closed
			if children==[]:
				print("Blocked or Dead")
				return False
			print("Children")
			print(children)
			listObject.clear()				# Clear every time to store latest value of safe neighbours
			for child in children:
				(a,b)=child
				listObject.append(heuristic(a,b))
			closed.append((x,y))
			max1=listObject.index(max(listObject))	#Index of Maximum number in list to know child which is safest
			# print(listObject,max1)
			if max1+1:
				p,q=children[max1]
				fringe.append((p,q))
				print("List")
				print(listObject)
				if minmax(m1, (p, q), False,fireset)!=True:		#Calling Fire for advancing it
					return False

	else:
		(fireset,m1)=expandFire(m1,fireset, 0.2)	#Expand Fire according to q value passed
		# print("Fire")
		# print(fireset)
		if fireset[-1]==child or fireset[-1]==m1.mazeCells[m1.dimension - 1][m1.dimension - 1]:
				print("Dead")
				return False
		else:
			minmax(m1,child,True,fireset) 	# Giving back chance to player to move
# This function is for checking whether a path exist from (0,dim-1) to (dim-1,0)
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

p = 0.2
dim = 5

(fireset,m1) = generateFireMaze(dim,p)
# goal=[]
(x,y)=(0,0)
# (e,f)=(0,m1.dimension-1)
for i in range(m1.dimension):
	print(m1.mazeCells[i])
print(minmax(m1,(x,y),True,fireset))
