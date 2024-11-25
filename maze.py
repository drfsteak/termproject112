# Name: David Li
# AndrewID: buyanl
# Section I

from maze_layout import maze
from cmu_graphics import *
import copy 

class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cellSize = width / len(maze[0])
        self.grid = copy.deepcopy(maze)

    def draw(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == 0:
                    drawRect(j * self.cellSize, i * self.cellSize, self.cellSize, self.cellSize, fill='black')
                elif self.grid[i][j] == 1:
                    drawRect(j * self.cellSize, i * self.cellSize, self.cellSize, self.cellSize, fill = 'blue')
                elif self.grid[i][j] == 2:
                    dotRadius = self.cellSize / 10
                    drawRect(j * self.cellSize, i * self.cellSize, self.cellSize, self.cellSize, fill='black')
                    drawCircle(j * self.cellSize + self.cellSize / 2, i * self.cellSize + self.cellSize / 2, dotRadius, fill='white')
                elif self.grid[i][j] == 3:
                    dotRadius = self.cellSize / 4
                    drawRect(j * self.cellSize, i * self.cellSize, self.cellSize, self.cellSize, fill='black')
                    drawCircle(j * self.cellSize + self.cellSize / 2, i * self.cellSize + self.cellSize / 2, dotRadius, fill='white')
    


    def getRowCol(self, x, y):
        row = int(y // self.cellSize)
        col = int(x // self.cellSize)
        return row, col

    def checkCollision(self, nextX, nextY):
        row, col = self.getRowCol(nextX, nextY)
        
        if (row < 0 or row >= len(self.grid) or 
            col < 0 or col >= len(self.grid[0])):
            return True  
        
        return self.grid[row][col] == 1

                


