import math;

def euclidDistance((x1,y1),(x2,y2)):
	return math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2));

def manhattanDistance((x1,y1),(x2,y2)):
	return math.fabs(x2-x1) + math.fabs(y2-y1);
