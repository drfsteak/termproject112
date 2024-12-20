# Name: David Li
# AndrewID: buyanl
# Section I

from cmu_graphics import *
from maze import Maze
class PacMan:
    def __init__(self, x, y, radius, mouthAngle, closing, direction = "right"):
        self.x = x
        self.y = y
        self.radius = radius
        self.mouthAngle = mouthAngle
        self.closing = closing
        self.direction = direction
        self.still = True
        self.score = 0
        self.nextDirection = direction
        self.blinkCount = 0
        self.blinkTimer = 0
        self.maxBlinks = 6
        self.blinkDuration = 10
        self.deathAnimationComplete = False
        self.poweredUp = False
        self.poweredUpDuration = 0


    # For loading screen pacmans
    # I used CSAcademy's Pacman section to help with the mouth staying within its bounds.
    def update(self):
        
        if self.closing:
            self.mouthAngle -= 10
            if self.mouthAngle == 0:
                self.closing = False
        else:
            self.mouthAngle += 10
            if self.mouthAngle == 90:
                self.closing = True
        
        
        if self.direction == 'right':
            self.x += 10
            if self.x - self.radius > app.width:
                pixelsBeyondRightEdgeOfCanvas = self.x + self.radius - app.width
                self.x = -self.radius + pixelsBeyondRightEdgeOfCanvas
        elif self.direction == 'left':
            self.x -= 10
            if self.x + self.radius < 0:
                pixelsBeyondLeftEdgeOfCanvas = self.x + self.radius
                self.x = app.width + self.radius - pixelsBeyondLeftEdgeOfCanvas
       


    def collectPellet(self, row, col):
        if app.maze.grid[row][col] == 2:
            self.score += 10
            app.chompSound.play()
            app.maze.grid[row][col] = 0
    
    def collectPowerPellet(self, row, col):
        if app.maze.grid[row][col] == 3:
            app.blinky.frightened = True
            app.clyde.frightened = True
            app.pinky.frightened = True
            self.poweredUp = True
            app.maze.grid[row][col] = 0

    # For updating PacMan when he is moving
    def update1(self):
        if self.still == False:
            if self.poweredUp:
                self.poweredUpDuration += 1
                if self.poweredUpDuration >= 150:
                    self.poweredUp = False
                    self.poweredUpDuration = 0
            if self.closing:
                self.mouthAngle -= 10
                if self.mouthAngle == 0:
                    self.closing = False
            else:
                self.mouthAngle += 10
                if self.mouthAngle == 90:
                    self.closing = True
            
            
            
            nextX = self.x
            nextY = self.y
            
            increment = 10
            check = 25
            Buffer = 15

            # First check if we can turn to the requested direction
            if self.nextDirection != self.direction:
                canTurn = False
                if self.nextDirection == 'right':
                    canTurn = (not app.maze.checkCollision(self.x + check, self.y) and
                             not app.maze.checkCollision(self.x + check, self.y + Buffer) and
                             not app.maze.checkCollision(self.x + check, self.y - Buffer))
                elif self.nextDirection == 'left':
                    canTurn = (not app.maze.checkCollision(self.x - check, self.y) and
                             not app.maze.checkCollision(self.x - check, self.y + Buffer) and
                             not app.maze.checkCollision(self.x - check, self.y - Buffer))
                elif self.nextDirection == 'up':
                    canTurn = (not app.maze.checkCollision(self.x, self.y - check) and
                             not app.maze.checkCollision(self.x + Buffer, self.y - check) and
                             not app.maze.checkCollision(self.x - Buffer, self.y - check))
                elif self.nextDirection == 'down':
                    canTurn = (not app.maze.checkCollision(self.x, self.y + check) and
                             not app.maze.checkCollision(self.x + Buffer, self.y + check) and
                             not app.maze.checkCollision(self.x - Buffer, self.y + check))
                
                if canTurn:
                    self.direction = self.nextDirection

            # Continue with normal movement using current direction
            if self.direction == 'right':
                nextX += check
            elif self.direction == 'left':
                nextX -= check
            elif self.direction == 'up':
                nextY -= check
            elif self.direction == 'down':
                nextY += check

            # Check if the next position is a wall, if not, move there
            if not app.maze.checkCollision(nextX, nextY):
                self.still = False
                if self.direction == 'right':
                    self.x += increment
                elif self.direction == 'left':
                    self.x -= increment
                elif self.direction == 'up':
                    self.y -= increment
                elif self.direction == 'down':
                    self.y += increment
                
                # Check if the next position is a pellet or power pellet, if so, collect it
                row, col = app.maze.getRowCol(self.x, self.y)
                self.collectPellet(row, col)
                self.collectPowerPellet(row, col)
                if self.poweredUp:
                    app.blinky.color = 'blue'
                    app.clyde.color = 'blue'
                    app.pinky.color = 'blue'
                    app.inky.color = 'blue'
                    
                else:
                    app.blinky.frightened = False
                    app.clyde.frightened = False
                    app.pinky.frightened = False
                    app.clyde.color = 'orange'
                    app.blinky.color = 'red'
                    app.pinky.color = 'pink'
                    app.inky.color = 'cyan'
            else:
                self.still = True

    # For drawing PacMan when he is moving in all directions
    def drawMovement(self, mouthAngle):
        startAngle = int(mouthAngle/2)
        sweepAngle = int(360 - mouthAngle)
        if sweepAngle >= 360:
            sweepAngle = 359

        if self.direction == 'right':
            drawArc(self.x, self.y, self.radius, self.radius,
                   startAngle, sweepAngle, fill='yellow', border='black')
        elif self.direction == 'left':  
            drawArc(self.x, self.y, self.radius, self.radius,
                   startAngle + 180, sweepAngle, fill='yellow', border='black')
        elif self.direction == 'up':
            drawArc(self.x, self.y, self.radius, self.radius,
                   startAngle + 90, sweepAngle, fill='yellow', border='black')
        elif self.direction == 'down':
            drawArc(self.x, self.y, self.radius, self.radius,
                   startAngle + 270, sweepAngle, fill='yellow', border='black')
            
    
    # Loading Screen Pacmans (Pacmen?)
    def draw(self, width, mouthAngle):

        startAngle = mouthAngle/2
        sweepAngle = 360 - mouthAngle
        
        if self.direction == 'right':
            drawArc(self.x, self.y, self.radius, self.radius,
                   startAngle, sweepAngle, fill='yellow', border='black')
            
            if self.x + self.radius > width:
                pixelsBeyondRightEdgeOfCanvas = self.x + self.radius - width
                cx = -self.radius + pixelsBeyondRightEdgeOfCanvas
                drawArc(cx, self.y, self.radius, self.radius,
                       startAngle, sweepAngle, fill='yellow', border='black')
                
        else:  
            drawArc(self.x, self.y, self.radius, self.radius,
                   startAngle + 180, sweepAngle, fill='yellow', border='black')
            
            if self.x - self.radius < 0:
                pixelsBeyondLeftEdgeOfCanvas = self.x - self.radius
                cx = width + self.radius - pixelsBeyondLeftEdgeOfCanvas
                drawArc(cx, self.y, self.radius, self.radius,
                       startAngle + 180, sweepAngle, fill='yellow', border='black')
             
    # Death animation for PacMan, it blinks by by only drawing when the blinkCount is even
    def drawBlinking(self):
        if not self.deathAnimationComplete:  # During blinking animation
            if (self.blinkCount) % 2 == 0:
                startAngle = int(self.mouthAngle/2)
                sweepAngle = int(360 - self.mouthAngle)
                drawArc(self.x, self.y, self.radius, self.radius,
                       startAngle, sweepAngle, fill='yellow', border='black')
       
    # Update the death animation
    def updateDeath(self):
        if not self.deathAnimationComplete:
            self.blinkTimer += 1
            if self.blinkTimer >= self.blinkDuration:
                self.blinkTimer = 0
                self.blinkCount += 1
                if self.blinkCount >= self.maxBlinks:
                    self.deathAnimationComplete = True

