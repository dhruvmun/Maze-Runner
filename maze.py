import random

class Maze:
	# int dimension;
	# float probability;
	# list mazeCells;

	def __init__(self, dim, p):
		self.dimension = dim
		self.probability = p
		self.mazeCells = []
		for i in range(self.dimension):
			self.mazeCells.append([])
			for j in range(self.dimension):
				if (random.uniform(0, 1) <= self.probability):
					self.mazeCells[i].append(1)
				else:
					self.mazeCells[i].append(0)
		self.mazeCells[0][0] = 0
		self.mazeCells[self.dimension-1][self.dimension-1] = 0


	def giveEligibleChild(self, x, y):
		children=[]
		if x-1 >= 0:
			if self.mazeCells[x-1][y]==0:
				children.append((x-1,y))
		if x+1<=self.dimension-1:
			if self.mazeCells[x+1][y]==0:
				children.append((x+1,y))
		if y-1>=0:
			if self.mazeCells[x][y-1]==0:
				children.append((x,y-1))
		if y+1<=self.dimension-1:
			if self.mazeCells[x][y+1]==0:
				children.append((x,y+1))
		return children

	def BFS(self):
		fringe = [[(0, 0)]]  # Initial Start node of Matrix which is also the path traversed till now
		closedSet = []

		while len(fringe) != 0:		#Fringe not empty execute
			recent_Path = fringe.pop(0)		#Dequeue the first element of Fringe
			(x,y)=recent_Path[-1]		# (x,y) will be the last node of element dequeued from which we want to continue our path
			# x,y=state
			# print(recent_path)

			if (x,y) not in closedSet:
				childList = self.giveEligibleChild(x,y)		#Generate Eligible Children(Unblocked) if not in closed set
				# print(childList)
				for child in childList:
					new_Path = list(recent_Path)			#New list to append in fringe after adding the child
					new_Path.append(child)
					fringe.append(new_Path)
					# return path if neighbour is goal
					if child == (self.dimension-1,self.dimension-1):  #If child is goal return the new list
						return new_Path
				closedSet.append((x,y))						#Mark last node of element dequeued as Visited

		# print(recent_Path)
		return False								# Return False if goal not found


	def treeSearch(self, (startx, starty), (endx , endy)):
		fringe = [(startx,starty, [(startx, starty)])];
		closedSet = [];
		while (len(fringe) != 0):
			(x, y, path) = fringe.pop();
			if (x,y) not in closedSet:
				if (x,y) == (endx,endy):
					return path;
				eligibleChildren = self.giveEligibleChild(x,y);
				for (cx,cy) in eligibleChildren:
					fringe.append((cx,cy,path + [(cx,cy)]));
				closedSet.append((x,y));
		return [];


# m=Maze(15,0.5)
# # print(m.mazeCells)
# for row in m.mazeCells:
# 	print(row)
# print(m.BFS())

	def bidirection(self):
		fringe1 = [[(0, 0)]]
		fringe2 = [[(self.dimension - 1, self.dimension - 1)]]
		closed1 = {(0, 0): True}
		closed2 = {(self.dimension - 1, self.dimension - 1): True}
		while fringe1 and fringe2:
			if fringe1:
				recent_path1 = fringe1.pop(0)
				(x, y) = recent_path1[-1]
				children = self.giveEligibleChild(x, y)
				for child in children:
					if child not in closed1:
						closed1[child] = True
						new_Path = list(recent_path1)  # New list to append in fringe after adding the child
						new_Path.append(child)
						fringe1.append(new_Path)
						if child == (self.dimension - 1, self.dimension - 1) or child in fringe2:
							return new_Path
			if fringe2:
				recent_path2 = fringe2.pop(0)
				(x, y) = recent_path2[-1]
				children = self.giveEligibleChild(x, y)
				for child in children:
					if child not in closed2:
						closed2[child] = True
						new_Path = list(recent_path2)  # New list to append in fringe after adding the child
						new_Path.append(child)
						fringe2.append(new_Path)
						if child == (self.dimension - 1, self.dimension - 1) or child in fringe11:
							return new_Path
		return False

	def dfs(self):

		goal_state = (self.dimension-1,self.dimension-1)
		fringe = [(0,0,[(0,0)])] #x,y,path
		closed_set = [] 
		
		while (len(fringe)):
			x,y,path = fringe.pop()
			current_state = (x,y)
			
			if(current_state not in closed_set):
				path.append(current_state)
				
				if (current_state == goal_state):
					return path

				children = self.giveEligibleChild(x,y)
				#print(children)
				
				for a,b in children:
					fringe.append((a,b,path))

				
				closed_set.append(current_state)
		return "NO SOLUTION"



