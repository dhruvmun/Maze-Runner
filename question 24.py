import maze
import helper
import matplotlib.pyplot as plt
import question23
import random
import helper_24



p0=question23.probability_threshold()           #Using Threshold Probability from previous question
prob=[round(random.uniform(0,p0),2) for _ in range(6)]  #Random Probability generated from 0 to p0
prob.sort()
dim=50
no_of_run=15        #No. of Runs for each probability
#List created for each Algorithm
bfs=[]
dfs=[]
bibfs=[]
euclid=[]
mann=[]
#Variables for each algorithm for calculating average
sumBfs=0
countBfs=0
sumDfs=0
countDfs=0
sumBibfs=0
countBibfs=0
sumEuclid=0
countEuclid=0
sumMann=0
countMann=0
#Calculated avg length of path for each algorithm
for p in prob:
    for k in range(no_of_run):
        a = maze.Maze(dim, p)
        bfs1 = len(a.BFS())         #Calculating length of path returned
        if bfs1 != 0:
            sumBfs += bfs1
            countBfs += 1
        dfs1 = len(a.dfs())         #Calculating length of path returned
        if dfs1!=0:
            sumDfs += dfs1
            countDfs += 1
        bibfs1 = len(a.bidirection())   #Calculating length of path returned
        if bibfs1!=0:
            sumBibfs += bibfs1
            countBibfs += 1
        euclid1 = len(a.aStarSearch(helper.euclidDistance)) #Calculating length of path returned
        if euclid1!=0:
            sumEuclid += euclid1
            countEuclid += 1
        mann1 = len(a.aStarSearch(helper.manhattanDistance))        #Calculating length of path returned
        if mann1!=0:
            sumMann += mann1
            countMann += 1
    # Calculating Avg for all the runs
    if countBfs!=0:
        bfs.append((sumBfs/countBfs))
    elif countBfs==0:
        bfs.append(countBfs)
    if countDfs != 0:
        dfs.append((sumDfs / countDfs))
    elif countDfs == 0:
        dfs.append(countBfs)
    if countBibfs != 0:
        bibfs.append((sumBibfs / countBibfs))
    elif countBibfs == 0:
        bibfs.append(countBibfs)
    if countEuclid != 0:
        euclid.append((sumEuclid / countEuclid))
    elif countEuclid == 0:
        euclid.append(countEuclid)
    if countMann != 0:
        mann.append((sumMann / countMann))
    elif countMann == 0:
        mann.append(countMann)

#Plotting graph between Avg Length and Density for each graph
plt.plot(prob, bfs,label='BFS')
plt.plot(prob, dfs,label='DFS')
plt.plot(prob,bibfs,label='BIBFS')
plt.plot(prob,euclid,label='Euclid')
plt.plot(prob,mann,label='Manhattan')
plt.ylabel('Average')
plt.xlabel('Density')
plt.title('Average vs Density')
plt.show()
closedSet()



def closedSet():        #Method to calculate length of closed set to compare all algorithms
    totalBfs=[]
    totalDfs=[]
    totalEuclid=[]
    totalMann=[]
    totalBidirection=[]
    closebfs=0
    closedfs=0
    closedBiBfs=0
    closedEuclid=0
    closedMann=0
    for p in prob:
        for k in range(no_of_run):
            b=helper_24.Maze_helper(dim,p)
            closebfs+=b.BFS()                   #Each Algorithm will return length of closed set
            closedfs+=b.dfs()
            closedBiBfs+=b.bidirection()
            closedEuclid+=b.aStarSearch(helper.euclidDistance)
            closedMann+=b.aStarSearch(helper.manhattanDistance)
        totalBfs.append(closebfs/no_of_run)
        totalDfs.append(closedfs/no_of_run)
        totalBidirection.append(closedBiBfs/no_of_run)
        totalEuclid.append((closedEuclid/no_of_run))
        totalMann.append(closedMann/no_of_run)


    bfsAvg=sum(totalBfs)/len(totalBfs)          #Calculating Average of closed set length for BFS
    dfsAvg=sum(totalDfs)/len(totalDfs)          #Calculating Average of closed set length for DFS
    Bidir=sum(totalBidirection)/len(totalBidirection)   #Calculating Average of closed set length for BD-BFS
    Eucl=sum(totalEuclid)/len(totalEuclid)  #Calculating Average of closed set length for A* Euclid
    Mannt=sum(totalMann)/len(totalMann) #Calculating Average pf closed set length for A* Mannhattan
    print("bfs=" + str(bfsAvg))
    print("dfs=" + str(dfsAvg))
    print("bibfs=" + str(Bidir))
    print("Euclid=" + str(Eucl))
    print("Manhattan=" + str(Mannt))
