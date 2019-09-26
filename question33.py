import maze
import visualization
import hardMaze

## DFS with Max fringe length

# hard = hardMaze.beamSearch(20,0.35,5, hardMaze.aStarWithDistanceFunction, hardMaze.manhattanDistanceWithMaximalNodes)

# visualise = visualization.Visualize("DFS", 'yellow', 0, 0)
# print "Score:" + str(-hard[0])
# visualise.drawMaze(hard[1])
# x = raw_input()

dfsWFringe = hardMaze.beamSearch(20,0.35,5, hardMaze.dfsWithMaxFringe, hardMaze.dfsWithMaxFringeLength)

visualise = visualization.Visualize("BFS", 'yellow', 0, 320)
visualise.drawMaze(dfsWFringe[1])
(path, closedSet) = dfsWFringe[1].treeSearch()
visualise.drawPath(path)
color = 'red'
visualise.drawPath(closedSet, color)
print "Score:" + str(-dfsWFringe[0])
x = raw_input()