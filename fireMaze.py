import maze

# 0->Open, 1->Block, 2->fire
mazeObject = maze.Maze(dim, p)
mazeObject.mazeCells[0][dim-1] = 2


# 1−(1−q)^k  k:neighbours, q:flamability
def giveFireChild(x, y, q, p0):
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


def Fire(fireset):
	for i in range(len(fireset)):
		(x,y) = fireset[i]
		if(x-1>=0 and mazeObject.mazeCells[x-1][y]==0):	#Blocked cell cannot catch fire
			giveFireChild(x-1,y,q,p0)
		if(x+1<=dim-1 and mazeObject.mazeCells[x+1][y]==0):
			giveFireChild(x-1,y,q,p0)
		if(y-1>=0 and mazeObject.mazeCells[x][y-1]==0):
			giveFireChild(x-1,y,q,p0)
		if(y+1<=dim-1 and mazeObject.mazeCells[x][y+1]==0):
			giveFireChild(x-1,y,q,p0)
		
