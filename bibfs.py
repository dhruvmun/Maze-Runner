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
    '''
    def bi_bfs(self):
        source_state = (0,0)
        goal_state = (self.dimension-1,self.dimension-1)

        fringe1 = [source_state]
        fringe2 = [goal_state]

        closed_set1 = []
        closed_set2 = []

        while len(fringe1) and len(fringe2):
            if(len(fringe1)):
                x1,y1 = fringe1.pop(0)
                current_state1 = (x1,y1)

                if current_state1 not in closed_set1:
                    #path1.append(current_state1)

                    if current_state1 == goal_state or 
                        print("Meeting point:" + str(current_state1))
                        return "Success"

                    children1 = self.giveEligibleChild(x1,y1)
                    for a,b in children1:
                        fringe1.append((a,b))

                    closed_set1.append(current_state1)
                    

            if(len(fringe2)):
                x2,y2 = fringe2.pop(0)
                current_state2 = (x2,y2)

                if current_state2 not in closed_set2:
                    #path2.append(current_state2)

                    if current_state2 == source_state or current_state2 in fringe1:
                        print("Meeting point:" + str(current_state2))
                        return "Success"

                    children2 = self.giveEligibleChild(x2,y2)
                    for a,b in children2:
                        fringe2.append((a,b))

                    closed_set2.append(current_state2)    

        return "No solution"
        '''
    def bidir(self):
        q1=[[(0,0)]]
        q2=[[(self.dimension-1,self.dimension-1)]]
        closed1={(0,0):True}
        closed2={(self.dimension-1,self.dimension-1):True}
        while q1 and q2:
            if q1:
                r1=q1.pop(0)
                (x,y)=r1[-1]
                children=self.giveEligibleChild(x,y)
                for child in children:
                    if child not in closed1:
                          closed1[child]=True
                          new_Path = list(r1)  # New list to append in fringe after adding the child
                          new_Path.append(child)
                          q1.append(new_Path)
                          if child == (self.dimension - 1, self.dimension - 1) or child in q2:
                              return new_Path
            if q2:
                r2 = q2.pop(0)
                (x, y) = r2[-1]
                children = self.giveEligibleChild(x, y)
                for child in children:
                    if child not in closed2:
                        closed2[child] = True
                        new_Path = list(r2)  # New list to append in fringe after adding the child
                        new_Path.append(child)
                        q2.append(new_Path)
                        if child == (self.dimension - 1, self.dimension - 1) or child in q1:
                            return new_Path
        return False

x = Maze(10, 0.3)
for row in x.mazeCells:
    print row

print x.bidir()            
               
                