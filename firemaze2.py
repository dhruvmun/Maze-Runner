import maze
import helper
import matplotlib.pyplot as plt


def neighbourOnFire(x,y):
	k = 0
	if(x-1>=0 and mazeObject.mazeCells[x-1][y]==2):	#Blocked cell cannot catch fire
		k+=1
	if(x+1<=dim-1 and mazeObject.mazeCells[x+1][y]==2):
		k+=1
	if(y-1>=0 and mazeObject.mazeCells[x][y-1]==2):
		k+=1
	if(y+1<=dim-1 and mazeObject.mazeCells[x][y+1]==2):
		k+=1
	return k

def giveFireChild(mazeObject, fireset, x, y, q, p0):
	k = neighbourOnFire(x,y)	
	fireProb = 1-pow((1-q),k)
	if(fireProb>=p0):
		mazeObject.mazeCells[x][y]=2
		fireset.append((x,y))

def spreadFire(mazeObject, fireset, q):
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
		
def evaluate(x,y):
	k = neighbourOnFire(x,y)
	fireProb = 1-pow((1-q),k)
	return fireProb

def findPath(dim, p, q):
	mazeObject = maze.Maze(dim, p)
	mazeObject.mazeCells[0][dim-1] = 2
	fireset = [(0,dim-1)]

	current_state = (0,0)
	maxi = evaluate(x,y)
	next_state = current_state
	if x-1>=0 and mazeObject.mazeCells[x-1][y]==0:
		eva = evaluate(x-1,y)
		if eva>maxi:
			maxi=eva
			next_state = (x-1,y)
	if x+1<=dim-1 and mazeObject.mazeCells[x+1][y]==0:
		eva = evaluate(x+1,y)
		if eva>maxi:
			maxi=eva
			next_state = (x+1,y)
	if y-1>=0 and mazeObject.mazeCells[x][y-1]==0:
		eva = evaluate(x,y-1)
		if eva>maxi:
			maxi=eva
			next_state = (x,y-1)
	if y+1<dim-1 and mazeObject.mazeCells[x][y+1]==0:
		eva = evaluate(x,y+1)
		if eva>maxi:
			maxi=eva
			next_state = (x,y+1)

	current_state = next_state
	spreadFire(mazeObject, fireset, q)

