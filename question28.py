import maze
import helper
import helper_24

dim=75
p=0.3
maze1=helper_24.Maze_helper(dim,p)
euclid=maze1.aStarSearch(helper.euclidDistance)
mann=maze1.aStarSearch(helper.manhattanDistance)
bibfs=maze1.bidirection()

print(euclid)
print(mann)
print(bibfs)

