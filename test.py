import maze;
import helper;
import time
import turtle
import visualization


# mazeObject.treeSearch((0,0),(n-1,n-1));
# b = mazeObject.BFS()

def temp():
	f = [(0,[])];
	while (len(f) !=0):
		print f;
		(x,p) = f.pop();
		if x == 4:
			return;
		p.append(x);
		t = [x-1,x+1];
		for (cx) in t:
			f.append((cx,p));
	return;

def temp2():
	f = [(0,[])];
	for i in range(4):
		print f;
		(x,p) = f.pop();
		p.append(x);
		t = [x-1,x+1];
		for (cx) in t:
			f.append((cx,p));
	return;

# mazeObject = maze.Maze(10, 0.3)
# scale = 15
# t = turtle.getturtle()
# visualization.setTurtle(t)
# for row in mazeObject.mazeCells:
# 	print row;
# visualization.drawMaze(mazeObject,t,scale)
# path = mazeObject.aStarSearch((0,0),(mazeObject.dimension-1,mazeObject.dimension-1),helper.euclidDistance)
# print path
# visualization.drawPath(path, t, scale, 'yellow')
# p = raw_input()
