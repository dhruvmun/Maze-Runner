import maze
import helper
import matplotlib.pyplot as plt
import question23
import random
import helper_24



p0=question23.probability_threshold()
prob=[round(random.uniform(0,p0),2) for _ in range(6)]
prob.sort()
dim=50
no_of_run=15
bfs=[]
dfs=[]
bibfs=[]
euclid=[]
mann=[]
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

def closedSet():
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
            closebfs+=b.BFS()
            closedfs+=b.dfs()
            closedBiBfs+=b.bidirection()
            closedEuclid+=b.aStarSearch(helper.euclidDistance)
            closedMann+=b.aStarSearch(helper.manhattanDistance)
        totalBfs.append(closebfs/no_of_run)
        totalDfs.append(closedfs/no_of_run)
        totalBidirection.append(closedBiBfs/no_of_run)
        totalEuclid.append((closedEuclid/no_of_run))
        totalMann.append(closedMann/no_of_run)


    bfsAvg=sum(totalBfs)/len(totalBfs)
    dfsAvg=sum(totalDfs)/len(totalDfs)
    Bidir=sum(totalBidirection)/len(totalBidirection)
    Eucl=sum(totalEuclid)/len(totalEuclid)
    Mannt=sum(totalMann)/len(totalMann)
    print("bfs=" + str(bfsAvg))
    print("dfs=" + str(dfsAvg))
    print("bibfs=" + str(Bidir))
    print("Euclid=" + str(Eucl))
    print("Manhattan=" + str(Mannt))

for p in prob:
    for k in range(no_of_run):
        a = maze.Maze(dim, p)
        bfs1 = len(a.BFS())
        if bfs1 != 0:
            sumBfs += bfs1
            countBfs += 1
        dfs1 = len(a.dfs())
        if dfs1!=0:
            sumDfs += dfs1
            countDfs += 1
        bibfs1 = len(a.bidirection())
        if bibfs1!=0:
            sumBibfs += bibfs1
            countBibfs += 1
        euclid1 = len(a.aStarSearch(helper.euclidDistance))
        if euclid1!=0:
            sumEuclid += euclid1
            countEuclid += 1
        mann1 = len(a.aStarSearch(helper.manhattanDistance))
        if mann1!=0:
            sumMann += mann1
            countMann += 1
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
# print(bfs)
# print(dfs)
# print(bibfs)
# print(euclid)
# print(mann)
closedSet()
plt.plot(prob, bfs,label='BFS')
plt.plot(prob, dfs,label='DFS')
plt.plot(prob,bibfs,label='BIBFS')
plt.plot(prob,euclid,label='Euclid')
plt.plot(prob,mann,label='Manhattan')
plt.ylabel('Average')
plt.xlabel('Density')
plt.title('Average vs Density')
plt.show()