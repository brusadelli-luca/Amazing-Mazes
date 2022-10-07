#Amazing Mazes
# Classes

import random

class Maze:
    def __init__(self,N):
        self.N = N

        self.cells = []
        for I in range(N):
            self.cells.append([])
            for J in range(N):
                self.cells[I].append(Cell(I,J))
    
        self.cells[0][0].walls['W'] = False
        self.cells[N-1][N-1].walls['E'] = False

    def __str__(self):
        wall = {True:'#', False:'.'}
        
        maze_out = ''

        for I in range(self.N):
            
            maze_out_W = ''
            maze_out_C = ''

            for J in range(self.N):

                maze_out_W = maze_out_W + '#' + wall[self.cells[I][J].walls['N']]
                maze_out_C = maze_out_C + wall[self.cells[I][J].walls['W']] + self.cells[I][J].symbol
            
            maze_out_W = maze_out_W + "#"
            maze_out_C = maze_out_C + wall[self.cells[I][J].walls['E']]
            maze_out = maze_out + '\n' + maze_out_W + '\n' + maze_out_C

        maze_out_W = ''
        for J in range(self.N):
            maze_out_W = maze_out_W + '#' + wall[self.cells[I][J].walls['S']]
        maze_out_W = maze_out_W + "#"
        
        maze_out = maze_out + '\n' + maze_out_W            

        return maze_out

    def Write(self,file_name):
        fichier = open(file_name + '.txt',"w")
        fichier.write(str(self))

    def available_dir(self,cell):
        dir_list = []
        if not (cell.X == 0 or self.cells[cell.X-1][cell.Y].visited == True):
            dir_list.append('N')
        if not (cell.Y == self.N-1 or self.cells[cell.X][cell.Y+1].visited == True):
            dir_list.append('E')
        if not (cell.X == self.N-1 or self.cells[cell.X+1][cell.Y].visited == True):
            dir_list.append('S')
        if not (cell.Y == 0 or self.cells[cell.X][cell.Y-1].visited == True):
            dir_list.append('W')
        return dir_list

class Cell:
    def __init__(self,X,Y):
        self.X = X
        self.Y = Y

        self.walls = {
                        'N' : True,
                        'E' : True,
                        'W' : True,
                        'S' : True
                        }

        self.symbol = '.'
        self.visited = False

    def __str__(self):
        wall = {True:'#', False:'.'}
        
        return ' ' + wall[self.walls['N']] + '\n' + wall[self.walls['W']] + self.symbol + wall[self.walls['E']] + '\n' + ' ' + wall[self.walls['S']]
    
    def ID(self):
        return [self.X, self.Y]

    def Visit(self):
        self.visited = True

    def walls_up(self):
        if False not in self.walls.values():
            return True
        else:
            return False

    def break_wall(self,dir):

        self.walls[dir] = False