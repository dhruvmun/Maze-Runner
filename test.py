import maze;
import helper;
n=1000
x = maze.Maze(n,0.2);
# for row in x.mazeCells:
	# print row;
# print x.treeSearch((0,0),(n-1,n-1));
# print x.treeSearch2((0,0),(4,4));
a =  x.aStarSearch((0,0),(n-1,n-1),helper.euclidDistance);
# b = x.BFS()

print len(a)
# print len(b)
# fringe = [[4]];

# for i in range(3):
# 	print fringe;
# 	p = fringe.pop();
# 	for j in range(3):
# 		fringe.append([j]);

# print fringe;

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

# temp2()
[0, 0, 0, 0, 1]
[0, 0, 0, 0, 0]
[0, 0, 1, 1, 1]
[1, 0, 0, 0, 1]
[0, 0, 1, 0, 0]
[(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (1, 4), (1, 2), (1, 1), (1, 0), (2, 0), (2, 1), (3, 1), (3, 2), (3, 3), (4, 3), (4, 4)]
[(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (1, 2), (1, 1), (1, 0), (2, 0), (2, 1), (3, 1), (3, 2), (3, 3), (4, 3), (4, 4)]