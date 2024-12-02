# Name: David Li
# AndrewID: buyanl
# Section I

from cmu_graphics import *
from pacman import PacMan
from maze import Maze
from ghost import Ghost, Blinky, Clyde, Pinky, Inky
# from mediapipeDemo import HandTracker (Not using external modules ATM)

def distance(x0, y0, x1, y1):
    return ((x0-x1)**2 + (y0-y1)**2)**0.5

def startPacMans(app):
    app.pacman1 = PacMan(0, app.height/4, 100, 90, True, direction='right')
    
    app.pacman2 = PacMan(app.width, 3*app.height/4, 100, 90, True, direction='left')
    app.gamePacman = PacMan(app.width/2, app.height/2 * 1.5 + 58, 32, 40, True, direction = "right")

def startGhosts(app):
    x, y = app.maze.getXY(10, 9)
    x += app.maze.cellSize / 2
    y += app.maze.cellSize / 2
    app.ghostStill = True
    app.counter = 0
    app.blinkyLeave = 0
    app.pinkyLeave = 30
    app.clydeLeave = 60
    app.blinky = Blinky(x-15, y, 14)
    app.clyde = Clyde(x+15, y, 14)
    app.pinky = Pinky(x+50, y, 14)
    app.inky = Inky(x-15, y, 14)

def sandBoxComponents(app):
    app.drawMode = True
    app.drawWall = False
    app.drawPacMan = False
    app.drawnPacMan = False

    app.drawPellet = False
    app.drawPowerPellet = False
    

def onAppStart(app):
    
    app.background = 'grey'
    app.width = 800
    app.height = 800
    app.maze = Maze(app.width, app.height)
    app.sandBoxMaze = Maze(app.width, app.height, True)
    startPacMans(app)
    startGhosts(app)
    app.url = '/Users/davidli/termproject112/images/download-removebg-preview (1).jpg' # https://logos-world.net/pacman-logo/
    app.start = False
    app.regularMode = False
    app.sandBoxMode = False
    sandBoxComponents(app)
    app.stepsPerSecond = 35
    app.instructions = False

    app.gameOver = False
    app.chompSound = Sound('https://eta.vgmtreasurechest.com/soundtracks/pac-man-game-sound-effects/knwtmadt/Chomp.mp3')
    app.sound = Sound('https://eta.vgmtreasurechest.com/soundtracks/pac-man-game-sound-effects/gmiffyvl/Intro.mp3')  # https://www.myinstants.com/en/instant/pacman-death-44465/
    app.deathSound = Sound('file:///Users/davidli/termproject112/sounds/pacman-die.mp3')  # https://www.myinstants.com/en/instant/pacman-death-44465/
    app.poweredUpSound = Sound('file:///Users/davidli/termproject112/sounds/pac-man-power-pellet.mp3') # https://www.myinstants.com/en/instant/pac-man-power-pellet-66997/
    app.eatingGhostSound = Sound('https://eta.vgmtreasurechest.com/soundtracks/pac-man-game-sound-effects/zaehkcsz/Ghost.mp3')
    app.gameOverImage = '/Users/davidli/termproject112/images/download.jpeg' # https://www.pond5.com/stock-footage/item/45769390-game-over-spin-down-arcade-end-game-screen-color-motion-grap
    app.InstructionsImage = '/Users/davidli/termproject112/images/text-1733076606719-removebg-preview.jpg' # Public Pixel Font by GGBotNet
    app.instructionsButton = '/Users/davidli/termproject112/images/images-removebg-preview.jpg' # https://www.kindpng.com/imgv/immwwoR_instructions-button-png-transparent-png/

def resetGame(app):
    app.background = 'grey'
    app.width = 800
    app.height = 800
    app.maze = Maze(app.width, app.height)
    app.sandBoxMaze = Maze(app.width, app.height, True)
    startPacMans(app)
    startGhosts(app)
    app.url = '/Users/davidli/termproject112/images/download-removebg-preview (1).jpg' # https://logos-world.net/pacman-logo/
    app.start = False
    app.regularMode = False
    app.sandBoxMode = False
    sandBoxComponents(app)
    app.stepsPerSecond = 35
    app.instructions = False

    app.gameOver = False
    app.chompSound = Sound('https://eta.vgmtreasurechest.com/soundtracks/pac-man-game-sound-effects/knwtmadt/Chomp.mp3')
    app.sound = Sound('https://eta.vgmtreasurechest.com/soundtracks/pac-man-game-sound-effects/gmiffyvl/Intro.mp3')  # https://www.myinstants.com/en/instant/pacman-death-44465/
    app.deathSound = Sound('file:///Users/davidli/termproject112/sounds/pacman-die.mp3')  # https://www.myinstants.com/en/instant/pacman-death-44465/
    app.poweredUpSound = Sound('file:///Users/davidli/termproject112/sounds/pac-man-power-pellet.mp3') # https://www.myinstants.com/en/instant/pac-man-power-pellet-66997/
    app.eatingGhostSound = Sound('https://eta.vgmtreasurechest.com/soundtracks/pac-man-game-sound-effects/zaehkcsz/Ghost.mp3')
    app.gameOverImage = '/Users/davidli/termproject112/images/download.jpeg' # https://www.pond5.com/stock-footage/item/45769390-game-over-spin-down-arcade-end-game-screen-color-motion-grap
    app.InstructionsImage = '/Users/davidli/termproject112/images/text-1733076606719-removebg-preview.jpg' # Public Pixel Font by GGBotNet

    app.instructionsButton = '/Users/davidli/termproject112/images/images-removebg-preview.jpg' # https://www.kindpng.com/imgv/immwwoR_instructions-button-png-transparent-png/


def redrawAll(app):
    if app.gameOver == False and app.gamePacman.poweredUp == False and app.start == False:
        app.sound.play()
    elif app.gameOver == False and app.gamePacman.poweredUp == True:
        app.poweredUpSound.play()
    
    if app.start == False and app.instructions == False:
        drawImage(app.url, app.width/2, app.height/2 - 100, align='center', width=450, height=200)
        drawImage(app.instructionsButton, app.width-50, app.height-50, align='center', width=175, height=100)
        app.pacman1.draw(app.width, app.pacman1.mouthAngle)
        app.pacman2.draw(app.width, app.pacman2.mouthAngle)
        
        drawRect(app.width/2 - 250, app.height/2 + 15, 200, 100, 
                fill=None, border='black', borderWidth=3)
        drawLabel('Regular Mode', app.width/2 - 150, app.height/2 + 65, 
                size=25, bold=True, align='center', fill = 'yellow', border = 'black', borderWidth = 1)
        drawRect(app.width/2 + 50, app.height/2 + 15, 200, 100, 
                fill=None, border='black', borderWidth=3)
        drawLabel('Sandbox Mode', app.width/2 + 150, app.height/2 + 65, 
                size=25, bold=True, align='center', fill = 'yellow', border = 'black', borderWidth = 1)
    elif app.regularMode == True:
        
        app.maze.draw()
        if app.gameOver:
            app.gamePacman.drawBlinking()
            if app.gamePacman.deathAnimationComplete:
                drawRect(0, 0, app.width, app.height, fill='black')
                drawImage(app.gameOverImage, app.width/2, app.height/2, align='center', width=450, height=200)
                drawLabel(f'Your Score: {app.gamePacman.score}', app.width/2, app.height/2 + 50, size=20, bold=True, align='center', fill = 'white')
                drawLabel('Press R to Restart', app.width/2, app.height/2 + 100, size=20, bold=True, align='center', fill = 'white')
        else:
            if app.blinky.returningToBase == False:
                app.blinky.draw()
            else:
                app.blinky.drawEyes()
            if app.clyde.returningToBase == False:
                app.clyde.draw()
            else:
                app.clyde.drawEyes()
            if app.pinky.returningToBase == False:
                app.pinky.draw()
            else:
                app.pinky.drawEyes()
            app.gamePacman.drawMovement(app.gamePacman.mouthAngle)
    elif app.sandBoxMode == True:
        app.sandBoxMaze.draw()
        if app.drawnPacMan:
            app.gamePacman.drawMovement(app.gamePacman.mouthAngle)
        
        for i in range(6):         
            
            if (i == 0 and app.drawWall) or (i == 1 and app.drawPacMan):
                borderColor = 'blue' 
            else:
                borderColor = 'white'
            drawRect(225 + i * (50 + 10), app.height - 50, 50, 50, 
                    fill='gray', border=borderColor)
    elif app.instructions:
        drawImage(app.InstructionsImage, app.width/2, 100, align='center', width=500, height=80)
        
        drawLabel('Welcome to Pac-man!', app.width/2, 175, align='center', size=20, fill='white')
        drawLabel('Navigate a maze and eat pellets to gain points while avoiding ghosts.',  app.width/2, 250, align='center', size=20, fill='white')
        drawLabel('Use the arrow keys to move Pac-man up, down, left, and right.', app.width/2, 325, align='center', size=20, fill='white')
        drawLabel('Each small pellet is worth 10 points.', app.width/2, 400, align='center', size=20, fill='white')
        drawLabel('Power pellets let you eat ghosts for points.', app.width/2, 475, align='center', size=20, fill='white')
        drawLabel('Ghosts will turn blue when you can eat them.', app.width/2, 550, align='center', size=20, fill='white')
        drawLabel('Avoid the ghosts! Getting caught ends your game.', app.width/2, 625, align='center', size=20, fill='white')

def onStep(app):
    if not app.gameOver:
        if app.regularMode:
            app.gamePacman.update1()
            
            # Checks if PacMan has collided with any ghosts
            dist = (app.gamePacman.radius + app.blinky.radius)/2
            if distance(app.gamePacman.x, app.gamePacman.y, app.blinky.x, app.blinky.y) < dist and app.blinky.returningToBase == False: 
                if app.gamePacman.poweredUp == False:
                    app.gameOver = True
                    app.deathSound.play()
                else:
                    app.eatingGhostSound.play()
                    app.blinky.returningToBase = True
     
            elif distance(app.gamePacman.x, app.gamePacman.y, app.clyde.x, app.clyde.y) < dist and app.clyde.returningToBase == False:
                if app.gamePacman.poweredUp == False:
                    app.gameOver = True
                    app.deathSound.play()
                else:
                    app.eatingGhostSound.play()
                    app.clyde.returningToBase = True
            elif distance(app.gamePacman.x, app.gamePacman.y, app.pinky.x, app.pinky.y) < dist and app.pinky.returningToBase == False:
                if app.gamePacman.poweredUp == False:
                    app.gameOver = True
                    app.deathSound.play()
                else:
                    app.eatingGhostSound.play()
                    app.pinky.returningToBase = True
            
            # Updating ghost movement based on their current state
            if app.ghostStill == False:

                app.counter += 1
                if app.blinky.returningToBase:
                    app.blinky.returnToBase()
                elif app.blinky.inBase:
                    app.blinky.moveOutBase()
                else:
                    if app.gamePacman.poweredUp:
                        app.blinky.frighten()
                    else:
                        app.blinky.turned = False
                        app.blinky.chase(app.gamePacman.x, app.gamePacman.y)

                if app.clyde.returningToBase:
                    app.clyde.returnToBase()
                elif app.clyde.inBase and app.counter > app.clydeLeave:
                    app.clyde.moveOutBase()
                else:
                    if app.gamePacman.poweredUp:
                        app.clyde.frighten()
                    else:
                        app.clyde.turned = False
                        app.clyde.chase()

                if app.pinky.returningToBase:
                    app.pinky.returnToBase()
                elif app.pinky.inBase and app.counter > app.pinkyLeave:
                    app.pinky.moveOutBase()
                else:
                    if app.gamePacman.poweredUp:
                        app.pinky.frighten()
                    else:
                        app.pinky.turned = False
                        app.pinky.chase(app.gamePacman.x, app.gamePacman.y)
        else:   
            # Loading screen Pacmans
            app.pacman1.update()
            app.pacman2.update()
    else:
        app.gamePacman.updateDeath()


def onKeyPress(app, key):
    if (app.sandBoxMode == True or app.regularMode == True) and key in ['up', 'down', 'right', 'left']:
        app.gamePacman.still = False
        app.ghostStill = False
        app.gamePacman.nextDirection = key
    if app.gameOver and key == 'r':
        resetGame(app)
    if app.sandBoxMode:
        if key == '1':
            app.drawWall = not app.drawWall
        elif key == '2':
            app.drawPacMan = not app.drawPacMan
            app.drawWall = False
        elif key == '3':
            app.drawPellet = not app.drawPellet
            app.drawPacMan = False
            app.drawWall = False
        elif key == '4':
            app.drawPowerPellet = not app.drawPowerPellet
            app.drawPacMan = False
            app.drawWall = False
            app.drawPellet = False



def onMousePress(app, mouseX, mouseY):
    if mouseX >= app.width/2 - 150 and mouseX <= app.width/2 + 150 and mouseY >= app.height/2 + 15 and mouseY <= app.height/2 + 115 and app.start == False:
        app.regularMode = True
        app.start = True
        app.stepsPerSecond = 20
    elif mouseX >= app.width/2 + 150 and mouseX <= app.width/2 + 350 and mouseY >= app.height/2 + 15 and mouseY <= app.height/2 + 115 and app.start == False:
        app.sandBoxMode = True
        app.background = 'black'
        app.start = True
        app.stepsPerSecond = 20
        app.height = 850 # expanding the height to fit the hotbar
    elif app.sandBoxMode: 
        if mouseY < app.height - 50:  # Not clicking in hotbar
            row, col = app.sandBoxMaze.getRowCol(mouseX, mouseY)
            
            if app.drawWall:
                app.sandBoxMaze.drawWall(row, col)
            elif app.drawPacMan:
                cellX = col * app.sandBoxMaze.cellSize + (app.sandBoxMaze.cellSize / 2)
                cellY = row * app.sandBoxMaze.cellSize + (app.sandBoxMaze.cellSize / 2)
                
                app.gamePacman = PacMan(cellX, cellY, 32, 40, True, direction="right")
                app.gamePacman.still = True
                app.drawnPacMan = True
            elif app.drawPellet:
                app.sandBoxMaze.drawPellet(row, col)
            elif app.drawPowerPellet:
                app.sandBoxMaze.drawPowerPellet(row, col)
    elif mouseX >= app.width-135 and mouseX <= app.width and mouseY >=app.height - 100 and mouseY <= app.height:
        app.instructions = True
        app.background = 'black'

def main():
    runApp()
    


main()