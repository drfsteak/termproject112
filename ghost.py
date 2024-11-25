# Name: David Li
# AndrewID: buyanl
# Section I

from cmu_graphics import *
from maze import Maze

class Ghost:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.frightened = False

    def draw(self):

        drawCircle(self.x, self.y, self.radius, fill=self.color)
        
       
        body_height = self.radius * 1.2
        drawRect(self.x - self.radius, self.y, 
                self.radius * 2, body_height,
                fill=self.color)
        
        wave_radius = self.radius / 3
        base_y = self.y + body_height
        for i in range(3):
            x_offset = self.x + (i - 1) * wave_radius * 2
            drawCircle(x_offset, base_y, 
                      wave_radius, fill=self.color)
        
        eye_radius = self.radius / 4
        eye_y = self.y - self.radius / 4
        
        drawCircle(self.x - self.radius/2, eye_y, 
                  eye_radius, fill='white')
        drawCircle(self.x - self.radius/2, eye_y, 
                  eye_radius/2, fill='blue')
        
        drawCircle(self.x + self.radius/2, eye_y, 
                  eye_radius, fill='white')
        drawCircle(self.x + self.radius/2, eye_y, 
                  eye_radius/2, fill='blue')
    
    def scatter(self, dx, dy):
        pass
    
    def frighten(self, dx, dy):
        pass

def distance(x0, y0, x1, y1):
    return ((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5

class Blinky(Ghost):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius, 'red')
        self.prev_direction = None
    
    def chase(self, pacman_x, pacman_y):
        targetRow, targetCol = app.maze.getRowCol(pacman_x, pacman_y)

        
        
        
        increment = 10
        check = 25
        Buffer = 15

        possible_moves = {
            'up': (self.x, self.y - check),
            'down': (self.x, self.y + check),
            'right': (self.x + check, self.y),
            'left': (self.x - check, self.y)
        }

        opposite_moves = {
            'up': 'down',
            'down': 'up',
            'left': 'right',
            'right': 'left'
        }

        best_direction = None
        min_distance = float('inf')

        for direction, (nextX, nextY) in possible_moves.items():
            if self.prev_direction and direction == opposite_moves[self.prev_direction]:
                continue
            
            canMove = True
            if direction in ['up', 'down']:
                canMove = (not app.maze.checkCollision(nextX, nextY) and
                          not app.maze.checkCollision(nextX + Buffer, nextY) and
                          not app.maze.checkCollision(nextX - Buffer, nextY))
            else:  
                canMove = (not app.maze.checkCollision(nextX, nextY) and
                          not app.maze.checkCollision(nextX, nextY + Buffer) and
                          not app.maze.checkCollision(nextX, nextY - Buffer))
            
            if not canMove:
                continue
            
            
            nextRow, nextCol = app.maze.getRowCol(nextX, nextY)
            dist = distance(nextRow, nextCol, targetRow, targetCol)            
            if dist < min_distance:
                min_distance = dist
                best_direction = direction

        if best_direction:
            self.prev_direction = best_direction
            if best_direction == 'up':
                self.y -= increment
            elif best_direction == 'down':
                self.y += increment
            elif best_direction == 'right':
                self.x += increment
            elif best_direction == 'left':
                self.x -= increment







        
        
        