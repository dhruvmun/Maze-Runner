import maze
import helper

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
	if(fireProb>p0):
		mazeObject.mazeCells[x][y]=2
		fireset.append((x,y))

def Fire(mazeObject, fireset, q):
	for i in range(len(fireset)):
		(x,y) = fireset[i]
		if(x-1>=0 and mazeObject.mazeCells[x-1][y]==0):	#Blocked cell cannot catch fire
			giveFireChild(mazeObject, fireset,x-1,y,q,p0)
		if(x+1<=dim-1 and mazeObject.mazeCells[x+1][y]==0):
			giveFireChild(mazeObject, fireset,x-1,y,q,p0)
		if(y-1>=0 and mazeObject.mazeCells[x][y-1]==0):
			giveFireChild(mazeObject, fireset,x-1,y,q,p0)
		if(y+1<=dim-1 and mazeObject.mazeCells[x][y+1]==0):
			giveFireChild(mazeObject, fireset,x-1,y,q,p0)
		

def findPath(p, q):
	# 0->Open, 1->Block, 2->fire
	mazeObject = maze.Maze(dim, p)
	mazeObject.mazeCells[0][dim-1] = 2
	fireset = [(0,dim-1)]

	shortestPath = mazeObject.aStarSearch(helper.euclidDistance)
	if shortestPath == []:
		return "No Path Exist"
	next_step = shortestPath.pop(0)
	if next_step == (dim-1,dim-1):
		return "Success"
	Fire(mazeObject, fireset, q)
	if next_step in fireset:
		return "Dead"

p0 = 0.7
dim = 20
a = findPath(0.2,0.2)
print a