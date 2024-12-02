# Name: David Li
# AndrewID: buyanl
# Section I

from cmu_graphics import *
from maze import Maze
import random

class Ghost:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.frightened = False
        self.prev_direction = None
        self.turned = False
        self.inBase = True
        self.speed = 10
        self.check = 25
        self.buffer = 15
        self.returningToBase = False

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
    
    def drawEyes(self):
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
    
    def moveOutBase(self):
        nextY = self.y - self.check

        if not app.maze.checkCollision2(self.x, nextY):
            self.y -= 5
        else:
            self.inBase = False
            

    def returnToBase(self):
        x, y = app.maze.getXY(10, 9)
        x += app.maze.cellSize / 2
        y += app.maze.cellSize / 2
        if (abs(self.x - x) <= 5 and abs(self.y - y) <= 5):
            self.returningToBase = False
            self.inBase = True
            self.frightened = False
            

        if self.x < x:
            self.x += self.speed
        elif self.x > x:
            self.x -= self.speed
        if self.y < y:
            self.y += self.speed
        elif self.y > y:
            self.y -= self.speed


   

    # Frightened algorithm from this video: https://www.youtube.com/watch?v=ataGotQ7ir8&t=227s
    # All the code is implemented by me, I did not view any external code for this function other than what was given in the chase function.
    def frighten(self):

     
        
        valid_moves = []
        opposite_moves = {
            'up': 'down',
            'down': 'up',
            'left': 'right',
            'right': 'left'
        }

        possible_moves = {
            'up': (self.x, self.y - self.check),
            'down': (self.x, self.y + self.check),
            'right': (self.x + self.check, self.y),
            'left': (self.x - self.check, self.y)
        }
        if self.turned == False:
            self.prev_direction = opposite_moves[self.prev_direction]

            if self.prev_direction == 'up':
                self.y -= self.speed
            elif self.prev_direction == 'down':
                self.y += self.speed
            elif self.prev_direction == 'right':
                self.x += self.speed
            elif self.prev_direction == 'left':
                self.x -= self.speed
            self.turned = True
        else:
            for direction, (nextX, nextY) in possible_moves.items():
                if direction == opposite_moves[self.prev_direction]:
                    continue
                
                canMove = True

                if direction in ['up', 'down']:
                    canMove = (not app.maze.checkCollision(nextX, nextY) and
                              not app.maze.checkCollision(nextX + self.buffer, nextY) and
                              not app.maze.checkCollision(nextX - self.buffer, nextY))
                else:
                    canMove = (not app.maze.checkCollision(nextX, nextY) and
                               not app.maze.checkCollision(nextX, nextY + self.buffer) and
                               not app.maze.checkCollision(nextX, nextY - self.buffer))
                
                if canMove:
                    valid_moves.append(direction)
            if len(valid_moves) == 0:
                nextMove = self.prev_direction
            else:
                nextMove = random.choice(valid_moves)

            self.prev_direction = nextMove
            if nextMove == 'up':
                self.y -= self.speed
            elif nextMove == 'down':
                self.y += self.speed
            elif nextMove == 'right':
                self.x += self.speed
            elif nextMove == 'left':
                self.x -= self.speed
        


        







def distance(x0, y0, x1, y1):
    return ((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5

class Pinky(Ghost):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius, 'pink')
    

    # https://www.youtube.com/watch?v=ataGotQ7ir8&t=423s Chase Algorithms for Different Ghosts
    # I watched the video to understand how the Ghost algorithm worked, but I implemented all the code myself

    # Pinky targets 4 spaces in front of PacMan, and has a special case when PacMan is facing up.
    def chase(self, pacman_x, pacman_y):
        targetRow, targetCol = app.maze.getRowCol(pacman_x, pacman_y)

        if app.gamePacman.direction == 'up':
            targetRow -= 4
            targetCol -= 4 # For some reason a programming quirk left in the original arcade PacMan left Pinky to target 4 spaces left of PacMan when PacMan's direction was up
        elif app.gamePacman.direction == 'down':
            targetRow += 4
        elif app.gamePacman.direction == 'right':
            targetCol += 4
        elif app.gamePacman.direction == 'left':
            targetCol -= 4
        
        
       
        
        possible_moves = {
            'up': (self.x, self.y - self.check),
            'down': (self.x, self.y + self.check),
            'right': (self.x + self.check, self.y),
            'left': (self.x - self.check, self.y)
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
                          not app.maze.checkCollision(nextX + self.buffer, nextY) and
                          not app.maze.checkCollision(nextX - self.buffer, nextY))
            else:  
                canMove = (not app.maze.checkCollision(nextX, nextY) and
                          not app.maze.checkCollision(nextX, nextY + self.buffer) and
                          not app.maze.checkCollision(nextX, nextY - self.buffer))
            
            if not canMove:
                continue
            
            
            nextRow, nextCol = app.maze.getRowCol(nextX, nextY)
            dist = distance(nextRow, nextCol, targetRow, targetCol)            
            if dist < min_distance:
                min_distance = dist
                best_direction = direction

     
        self.prev_direction = best_direction
        if best_direction == 'up':
            self.y -= self.speed
        elif best_direction == 'down':
            self.y += self.speed
        elif best_direction == 'right':
            self.x += self.speed
        elif best_direction == 'left':
            self.x -= self.speed
        
        


class Blinky(Ghost):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius, 'red')
    
    # https://www.youtube.com/watch?v=ataGotQ7ir8&t=423s Chase Algorithms for Different Ghosts
    # I did not know how to track the previous direction, so I asked ChatGPT how to store them. 
    def chase(self, pacman_x, pacman_y):
        targetRow, targetCol = app.maze.getRowCol(pacman_x, pacman_y)
       
      
     
        possible_moves = {
            'up': (self.x, self.y - self.check),
            'down': (self.x, self.y + self.check),
            'right': (self.x + self.check, self.y),
            'left': (self.x - self.check, self.y)
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
                          not app.maze.checkCollision(nextX + self.buffer, nextY) and
                          not app.maze.checkCollision(nextX - self.buffer, nextY))
            else:  
                canMove = (not app.maze.checkCollision(nextX, nextY) and
                          not app.maze.checkCollision(nextX, nextY + self.buffer) and
                          not app.maze.checkCollision(nextX, nextY - self.buffer))
            
            if not canMove:
                continue
            
            
            nextRow, nextCol = app.maze.getRowCol(nextX, nextY)
            dist = distance(nextRow, nextCol, targetRow, targetCol)            
            if dist < min_distance:
                min_distance = dist
                best_direction = direction

    
        self.prev_direction = best_direction
        if best_direction == 'up':
            self.y -= self.speed
        elif best_direction == 'down':
            self.y += self.speed
        elif best_direction == 'right':
            self.x += self.speed
        elif best_direction == 'left':
            self.x -= self.speed

class Inky(Ghost):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius, 'cyan')
    
    # Chase algorithm from this video: https://www.youtube.com/watch?v=ataGotQ7ir8&t=227s
    # All the code is implemented by me, I did not view any external code for this function other than what was given in the chase function.
    def chase(self, pacman_x, pacman_y, blinky_x, blinky_y):
        pacmanRow, pacmanCol = app.maze.getRowCol(pacman_x, pacman_y)

        if app.gamePacman.direction == 'up':
            pacmanRow -= 2
            pacmanCol -= 2 # For some reason a programming quirk left in the original arcade PacMan left Inky to target 2 spaces left of PacMan when PacMan's direction was up
        elif app.gamePacman.direction == 'down':
            pacmanRow += 2
        elif app.gamePacman.direction == 'right':
            pacmanCol += 2
        elif app.gamePacman.direction == 'left':
            pacmanCol -= 2
        
        blinkyRow, blinkyCol = app.maze.getRowCol(blinky_x, blinky_y)

        targetRow = pacmanRow + (pacmanRow - blinkyRow)
        targetCol = pacmanCol + (pacmanCol - blinkyCol)

        if targetRow < 0:
            targetRow = 0
        elif targetRow > app.maze.numRows - 1:
            targetRow = app.maze.numRows - 1
        if targetCol < 0:
            targetCol = 0
        elif targetCol > app.maze.numCols - 1:
            targetCol = app.maze.numCols - 1

        possible_moves = {
            'up': (self.x, self.y - self.check),
            'down': (self.x, self.y + self.check),
            'right': (self.x + self.check, self.y),
            'left': (self.x - self.check, self.y)
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
                          not app.maze.checkCollision(nextX + self.buffer, nextY) and
                          not app.maze.checkCollision(nextX - self.buffer, nextY))
            else:  
                canMove = (not app.maze.checkCollision(nextX, nextY) and
                          not app.maze.checkCollision(nextX, nextY + self.buffer) and
                          not app.maze.checkCollision(nextX, nextY - self.buffer))
            
            if not canMove:
                continue
            
            
            nextRow, nextCol = app.maze.getRowCol(nextX, nextY)
            dist = distance(nextRow, nextCol, targetRow, targetCol)            
            if dist < min_distance:
                min_distance = dist
                best_direction = direction

     
        self.prev_direction = best_direction
        if best_direction == 'up':
            self.y -= self.speed
        elif best_direction == 'down':
            self.y += self.speed
        elif best_direction == 'right':
            self.x += self.speed
        elif best_direction == 'left':
            self.x -= self.speed


class Clyde(Ghost):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius, 'orange')

    # https://www.youtube.com/watch?v=ataGotQ7ir8&t=423s Chase Algorithms for Different Ghosts
    # I watched the video to understand how the Ghost algorithm worked, but I implemented all the code myself aside from what was mentioned in Blinky's chase.
    def chase(self):
       
 
        valid_moves = []
        opposite_moves = {
            'up': 'down',
            'down': 'up',
            'left': 'right',
            'right': 'left'
        }

        possible_moves = {
            'up': (self.x, self.y - self.check),
            'down': (self.x, self.y + self.check),
            'right': (self.x + self.check, self.y),
            'left': (self.x - self.check, self.y)
        }

        for direction, (nextX, nextY) in possible_moves.items():
                if self.prev_direction and direction == opposite_moves[self.prev_direction]:
                    continue
                
                canMove = True

                if direction in ['up', 'down']:
                    canMove = (not app.maze.checkCollision(nextX, nextY) and
                              not app.maze.checkCollision(nextX + self.buffer, nextY) and
                              not app.maze.checkCollision(nextX - self.buffer, nextY))
                else:
                    canMove = (not app.maze.checkCollision(nextX, nextY) and
                               not app.maze.checkCollision(nextX, nextY + self.buffer) and
                               not app.maze.checkCollision(nextX, nextY - self.buffer))
                
                if canMove:
                    valid_moves.append(direction)
        if len(valid_moves) == 0:
            nextMove = self.prev_direction
        else:
            nextMove = random.choice(valid_moves)

        self.prev_direction = nextMove
        if nextMove == 'up':
            self.y -= self.speed
        elif nextMove == 'down':
            self.y += self.speed
        elif nextMove == 'right':
            self.x += self.speed
        elif nextMove == 'left':
            self.x -= self.speed

