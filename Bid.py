
    def bidir(self):
        q1=[[(0,0)]]
        q2=[[(self.dimension-1,self.dimension-1)]]
        closed1={(0,0):True}
        closed2={(self.dimension-1,self.dimension-1):True}
        while q1!=None and q2!=None:
            if q1!=None:
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
            if q2!=None:
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