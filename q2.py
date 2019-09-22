import maze

### For p ≈ 0.2, generate a solvable map, and show the paths returned for each algorithm. Do the results
### make sense? ASCII printouts are fine, but good visualizations are a bonus

x = maze.Maze(10,0.2)
for row in x.maze.mazeCells:
	print row

print("************ DFS Solution **************")
print(maze.dfs)
print("************ BFS Solution **************")
print(maze.bfs)
print("************ Bidirectional BFS Solution **************")
print(maze.bibfs)
print("************ A_star with Euclian distance Solution **************")
print(maze.astar_euc)
print("************ DFS Solution **************")
print(maze.astar_man)


