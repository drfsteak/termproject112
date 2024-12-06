# Name: David Li
# AndrewID: buyanl
# Section I

from collections.abc import Iterable
from maze_layout import maze, maze2
from cmu_graphics import *
import copy 

class Maze:
    def __init__(self, width, height, sandBox = False):
        self.width = width
        self.height = height
        self.cellSize = width / len(maze[0])
        
        if sandBox:
            self.grid = copy.deepcopy(maze2)
        else:
            self.grid = copy.deepcopy(maze)

    def draw(self):
        # Draw existing cells first
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
                elif self.grid[i][j] == 4:
                    drawRect(j * self.cellSize, i * self.cellSize, self.cellSize, self.cellSize, fill='white', border = 'lightGray')
        
        if app.sandBoxMode and app.drawMode:
            for j in range(len(self.grid[0]) + 1):
                x = j * self.cellSize
                drawLine(x, 0, x, self.height, fill='gray', opacity=30)
            
            for i in range(len(self.grid) + 1):
                y = i * self.cellSize
                drawLine(0, y, self.width, y, fill='gray', opacity=30)

 
    

    def getRowCol(self, x, y):
        row = int(y // self.cellSize)
        col = int(x // self.cellSize)
        return row, col
    
    def getXY(self, row, col):
        x = col * self.cellSize
        y = row * self.cellSize
        return x, y
    
    # For checking walls and gates
    def checkCollision(self, nextX, nextY):
        row, col = self.getRowCol(nextX, nextY)
        
        if (row < 0 or row >= len(self.grid) or 
            col < 0 or col >= len(self.grid[0])):
            return True  
        
        return self.grid[row][col] == 1  or self.grid[row][col] == 4
    
    # For checking walls only
    def checkCollision2(self, nextX, nextY):
        row, col = self.getRowCol(nextX, nextY)
        
        if (row < 0 or row >= len(self.grid) or 
            col < 0 or col >= len(self.grid[0])):
            return True  
        
        return self.grid[row][col] == 1

    def drawWall(self, row, col):
    
        if (self.grid[row][col] == 0 and 0 <= row < len(self.grid) and 0 <= col < len(self.grid[0])):    
            self.grid[row][col] = 1
    
    def drawPellet(self, row, col):
        if (self.grid[row][col] == 0 and 0 <= row < len(self.grid) and 0 <= col < len(self.grid[0])):    
            self.grid[row][col] = 2
    
    def drawPowerPellet(self, row, col):
        if (self.grid[row][col] == 0 and 0 <= row < len(self.grid) and 0 <= col < len(self.grid[0])):    
            self.grid[row][col] = 3
    
    def drawEraser(self, row, col):
        if (0 <= row < len(self.grid) and 0 <= col < len(self.grid[0])):    
            self.grid[row][col] = 0

                


