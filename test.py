import maze;
import helper;
import time
import turtle
import visualization
import hardMaze
import matplotlib.pyplot as plt


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
# hardnessScore = mazeObject.hardnessScore(helper.euclidDistance)
# print (hardnessScore)
# print path
# visualization.drawPath(path, t, scale, 'yellow')
# p = raw_input()

# x3 = [180,190,200,210,220,230,240,250,260,270]
# y3 = [17.8663908641,29.7374033133,29.1733769576,38.0184236368,18.7990829945,28.9901839097,42.2261126836,20.4956800143,59.9339116414,82.5470612844
# ]
# x2 = [180,190,200,210,220
# ]
# y2 = [24.1982336839,23.008163929,35.6381359895,36.5782150428,60.9820989768
# ]
x2 = [100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290]
y2 = [0.501469373703, 0.792354742686, 0.891753594081, 1.12269894282, 1.92779111862, 2.152440389, 2.75335407257, 4.08728202184, 4.30135424932, 6.59856208165, 9.51985367139, 10.391794761, 12.2002643744, 12.859871308, 16.4385949771, 24.7676796913, 25.5645627181, 31.1265106996, 35.2253803412, 45.6769379775]
plt.ylabel('TimeTaken')
plt.xlabel('Dimension')
plt.title('TimeTaken vs Dimension')
# plt.plot(x3,y3)
# plt.plot(x25,y25)
plt.plot(x2,y2)
plt.show()
