# Name: David Li
# AndrewID: buyanl
# Section I

from cmu_graphics import *
from pacman import PacMan
from maze import Maze
from ghost import Ghost, Blinky
# from mediapipeDemo import HandTracker (Not using external modules ATM)

def distance(x0, y0, x1, y1):
    return ((x0-x1)**2 + (y0-y1)**2)**0.5

def startPacMans(app):
    app.pacman1 = PacMan(0, app.height/4, 100, 90, True, direction='right')
    
    app.pacman2 = PacMan(app.width, 3*app.height/4, 100, 90, True, direction='left')
    app.gamePacman = PacMan(app.width/2, app.height/2 * 1.5 + 58, 32, 40, True, direction = "right")


def onAppStart(app):
    
    app.background = 'grey'
    app.width = 800
    app.height = 800
    app.maze = Maze(app.width, app.height)
    startPacMans(app)
    app.blinky = Blinky(220, 220, 14)
    app.url = '/Users/davidli/termproject112/images/download-removebg-preview (1).jpg'
    app.start = False
    app.regularMode = False
    app.aiMode = False
    app.stepsPerSecond = 35
    app.gameOver = False
    app.sound = Sound('https://eta.vgmtreasurechest.com/soundtracks/pac-man-game-sound-effects/gmiffyvl/Intro.mp3')
    app.deathSound = Sound('file:///Users/davidli/termproject112/sounds/pacman-die.mp3')
    app.gameOverImage = '/Users/davidli/termproject112/images/download.jpeg'

def resetGame(app):
    app.background = 'grey'
    app.width = 800
    app.height = 800
    app.maze = Maze(app.width, app.height)
    startPacMans(app)
    app.blinky = Blinky(220, 220, 14)
    app.url = '/Users/davidli/termproject112/images/download-removebg-preview (1).jpg'
    app.start = False
    app.regularMode = False
    app.aiMode = False
    app.stepsPerSecond = 35
    app.gameOver = False
    app.sound = Sound('https://eta.vgmtreasurechest.com/soundtracks/pac-man-game-sound-effects/gmiffyvl/Intro.mp3')
    app.deathSound = Sound('file:///Users/davidli/termproject112/sounds/pacman-die.mp3')
    app.gameOverImage = '/Users/davidli/termproject112/images/download.jpeg'

def redrawAll(app):
    if app.gameOver == False:
       app.sound.play()
    
    drawImage(app.url, app.width/2, app.height/2 - 100, align='center', width=450, height=200)
    if app.start == False:
        app.pacman1.draw(app.width, app.pacman1.mouthAngle)
        app.pacman2.draw(app.width, app.pacman2.mouthAngle)
        
        drawRect(app.width/2 - 250, app.height/2 + 15, 200, 100, 
                fill=None, border='blue', borderWidth=5)
        drawLabel('Regular Mode', app.width/2 - 150, app.height/2 + 65, 
                size=20, bold=True, align='center')
        drawRect(app.width/2 + 50, app.height/2 + 15, 200, 100, 
                fill=None, border='blue', borderWidth=5)
        drawLabel('AI Mode', app.width/2 + 150, app.height/2 + 65, 
                size=20, bold=True, align='center')
    elif app.aiMode == True or app.regularMode == True:
        
        app.maze.draw()
        if app.gameOver:
            app.gamePacman.drawBlinking()
            if app.gamePacman.deathAnimationComplete:
                drawRect(0, 0, app.width, app.height, fill='black')
                drawImage(app.gameOverImage, app.width/2, app.height/2, align='center', width=450, height=200)
                drawLabel(f'Your Score: {app.gamePacman.score}', app.width/2, app.height/2 + 50, size=20, bold=True, align='center', fill = 'white')
                drawLabel('Press R to Restart', app.width/2, app.height/2 + 100, size=20, bold=True, align='center', fill = 'white')
        else:
            app.blinky.draw()
            app.gamePacman.drawMovement(app.gamePacman.mouthAngle)

def onStep(app):
    if not app.gameOver:
        app.pacman1.update()
        app.pacman2.update()
        app.gamePacman.update1()
        app.blinky.chase(app.gamePacman.x, app.gamePacman.y)

        dist = (app.gamePacman.radius + app.blinky.radius)/2
        if distance(app.gamePacman.x, app.gamePacman.y, app.blinky.x, app.blinky.y) < dist and app.gamePacman.poweredUp == False:
            app.gameOver = True
            app.deathSound.play()
    else:
        app.gamePacman.updateDeath()


def onKeyPress(app, key):
    if (app.aiMode == True or app.regularMode == True) and key in ['up', 'down', 'right', 'left']:
        app.gamePacman.still = False
        app.gamePacman.nextDirection = key
    if app.gameOver and key == 'r':
        resetGame(app)


def onMousePress(app, mouseX, mouseY):
    if mouseX >= app.width/2 - 150 and mouseX <= app.width/2 + 150 and mouseY >= app.height/2 + 15 and mouseY <= app.height/2 + 115:
        app.regularMode = True
        app.start = True
        app.stepsPerSecond = 20
    elif mouseX >= app.width/2 + 150 and mouseX <= app.width/2 + 350 and mouseY >= app.height/2 + 15 and mouseY <= app.height/2 + 115:
        app.aiMode = True
        app.start = True
        app.stepsPerSecond = 20

    

def main():
    runApp()
    


main()