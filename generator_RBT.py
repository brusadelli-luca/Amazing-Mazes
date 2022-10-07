#Amazing Mazes
# Recursive Backtrack
from maze_classes import *

def build_recursive(maze):
    prev_wall = {
                'N' : 'S',
                'S' : 'N',
                'E' : 'W',
                'W' : 'E'
                }

    path = []
    cell = maze.cells[0][0]
    path.append(cell.ID())
    cell.Visit()

    cells_nb = maze.N * maze.N

    while len(path) < cells_nb:
        prev_X = cell.X
        prev_Y = cell.Y
        cell = next(maze,cell)
        
        if cell == 'END':
            i = -1
            while maze.available_dir(maze.cells[path[i][0]][path[i][1]]) == []:
                i = i - 1
            
            prev_X = path[i][0]
            prev_Y = path[i][1]
            cell = next(maze,maze.cells[path[i][0]][path[i][1]])
        
        if cell.X == prev_X:
            if cell.Y > prev_Y:
                dir = 'W'
            else:
                dir = 'E'

        elif cell.Y == prev_Y:
            if cell.X > prev_X:
                dir = 'N'
            else:
                dir = 'S'

        path.append(cell.ID())
        cell.Visit()
        cell.break_wall(dir)
        maze.cells[prev_X][prev_Y].break_wall(prev_wall[dir])
    
    return maze

def next(maze,cell):

    next_list = maze.available_dir(cell)
    if next_list != []:
        dir = random.choice(next_list)

        if dir == 'N' and cell.X > 0:
            return maze.cells[cell.X-1][cell.Y]

        elif dir == 'E' and cell.Y < maze.N - 1:
            return maze.cells[cell.X][cell.Y+1]

        elif dir == 'S' and cell.X < maze.N - 1:
            return maze.cells[cell.X+1][cell.Y]

        elif dir == 'W' and cell.Y > 0:
            return maze.cells[cell.X][cell.Y-1]

        else:
            return next(maze,cell)

    else:
        return 'END'