# Name: David Li
# AndrewID: buyanl
# Section I

from cmu_graphics import *
from pacman import PacMan
from maze import Maze
from ghost import Blinky, Clyde, Pinky, Inky
# from mediapipeDemo import HandTracker (Not using external modules ATM)

def distance(x0, y0, x1, y1):
    return ((x0-x1)**2 + (y0-y1)**2)**0.5

def startPacMans(app):
    app.pacman1 = PacMan(0, app.height/4, 100, 90, True, direction='right')
    
    app.pacman2 = PacMan(app.width, 3*app.height/4, 100, 90, True, direction='left')
    app.gamePacman = PacMan(app.width/2, app.height/2 * 1.5 + 58, 32, 40, True, direction = "right")

def resetComponents(app):
    app.drawWall = False
    app.drawPacMan = False
    app.drawEraser = False
    app.drawPellet = False
    app.drawPowerPellet = False
    
def startGhosts(app):
    x, y = app.maze.getXY(10, 9)
    x += app.maze.cellSize / 2
    y += app.maze.cellSize / 2
    app.ghostStill = True
    app.counter = 0
    app.pinkyLeave = 30
    app.clydeLeave = 60
    app.inkyLeave = 90
    app.blinky = Blinky(x-15, y - 3*app.maze.cellSize, 14)
    app.clyde = Clyde(x+15, y, 14)
    app.pinky = Pinky(x+50, y, 14)
    app.inky = Inky(x-15, y, 14)

def sandBoxComponents(app):
    app.drawMode = True
    app.drawWall = False
    app.drawPacMan = False
    app.drawnPacMan = False
    app.drawEraser = False
    app.drawPellet = False
    app.drawPowerPellet = False
    app.drawPopUp = False
    app.drawPopUp2 = False

def soundComponents(app):
    app.chompSound = Sound('https://eta.vgmtreasurechest.com/soundtracks/pac-man-game-sound-effects/knwtmadt/Chomp.mp3')
    app.sound = Sound('https://eta.vgmtreasurechest.com/soundtracks/pac-man-game-sound-effects/gmiffyvl/Intro.mp3')  # https://www.myinstants.com/en/instant/pacman-death-44465/
    app.deathSound = Sound('file:///Users/davidli/termproject112/sounds/pacman-die.mp3')  # https://www.myinstants.com/en/instant/pacman-death-44465/
    app.poweredUpSound = Sound('file:///Users/davidli/termproject112/sounds/pac-man-power-pellet.mp3') # https://www.myinstants.com/en/instant/pac-man-power-pellet-66997/
    app.eatingGhostSound = Sound('https://eta.vgmtreasurechest.com/soundtracks/pac-man-game-sound-effects/zaehkcsz/Ghost.mp3') # https://classicgaming.cc/classics/pac-man/sounds

def imageComponents(app):
    app.url = '/Users/davidli/termproject112/images/download-removebg-preview (1).jpg' # https://logos-world.net/pacman-logo/
    app.gameOverImage = '/Users/davidli/termproject112/images/download.jpeg' # https://www.pond5.com/stock-footage/item/45769390-game-over-spin-down-arcade-end-game-screen-color-motion-grap
    app.InstructionsImage = '/Users/davidli/termproject112/images/text-1733076606719-removebg-preview.jpg' # Public Pixel Font by GGBotNet
    app.instructionsButton = '/Users/davidli/termproject112/images/images-removebg-preview.jpg' # https://www.kindpng.com/imgv/immwwoR_instructions-button-png-transparent-png/
    app.restartImage = '/Users/davidli/termproject112/images/text-1733102813925-removebg-preview.jpg' # Public Pixel Font by GGBotNet           
    app.buttonImage = '/Users/davidli/termproject112/images/download (3)-removebg-preview.jpg' # https://www.freepik.com/premium-vector/pixel-art-stone-style-button-game-app-interface-vector-icon-8bit-game-white-background_28763371.htm
    app.popUpImage = '/Users/davidli/termproject112/images/Screenshot 2024-12-04 at 1.24.58 PM.png' # /Users/davidli/termproject112/images/Screenshot 2024-12-04 at 1.24.58 PM.png
    app.backArrowImage = '/Users/davidli/termproject112/images/download (1).png' # https://commons.wikimedia.org/wiki/File:Back_Arrow.svg
    app.inkyImage = '/Users/davidli/termproject112/images/Screenshot 2024-12-05 at 2.57.43 PM-removebg-preview.jpg' # https://www.pinterest.com/pin/pacman-ghosts-by-seingalad--640496378229925539/
    app.pinkyImage = '/Users/davidli/termproject112/images/Screenshot 2024-12-05 at 3.10.56 PM-removebg-preview.jpg' # https://www.pinterest.com/pin/pacman-ghosts-by-seingalad--640496378229925539/
    app.leftSpeechBubble = '/Users/davidli/termproject112/images/download (2)-removebg-preview.jpg' # https://commons.wikimedia.org/wiki/File:Speech_bubble.svg
    app.rightSpeechBubble = '/Users/davidli/termproject112/images/download (3)-removebg-preview (1).jpg' # https://www.vecteezy.com/free-vector/speech-bubble-outline
def onAppStart(app):
    app.background = 'grey'
    app.width = 800
    app.height = 800
    app.cx = 0
    app.cy = 0
    sandBoxComponents(app)
    app.maze = Maze(app.width, app.height)
    app.sandBoxMaze = Maze(app.width, app.height, True)
    startPacMans(app)
    startGhosts(app)
    app.start = False
    app.regularMode = False
    app.sandBoxMode = False
    
    app.stepsPerSecond = 35
    app.instructions = False

    app.gameOver = False
    soundComponents(app)
    imageComponents(app)

def resetGame(app):
    app.background = 'grey'
    app.width = 800
    app.height = 800
    app.maze = Maze(app.width, app.height)
    app.sandBoxMaze = Maze(app.width, app.height, True)
    startPacMans(app)
    startGhosts(app)
    app.start = False
    app.regularMode = False
    app.sandBoxMode = False
    sandBoxComponents(app)
    app.stepsPerSecond = 35
    app.instructions = False

    app.gameOver = False
    soundComponents(app)
    imageComponents(app)



def redrawAll(app):
    if app.gameOver == False and app.gamePacman.poweredUp == False and app.start == False:
        app.sound.play()
    elif app.gameOver == False and app.gamePacman.poweredUp == True:
        app.poweredUpSound.play()
    
    # Draw the main menu
    if app.start == False and app.instructions == False:
        drawImage(app.inkyImage, 100, app.height - 75, align='center', width=160, height=200)
        drawImage(app.leftSpeechBubble, 300, app.height - 100, align='center', width=300, height=150)
        drawLabel('My actual name is Bashful,', 315, app.height - 130, size=16, bold=True, align='center', fill='cyan', font ='caveat')
        drawLabel('but everyone calls me Inky!', 318, app.height - 100,size=16, bold=True, align='center', fill='cyan', font ='caveat')
        drawImage(app.pinkyImage, app.width - 100, 80, align='center', width=160, height=180)
        drawImage(app.rightSpeechBubble, app.width - 350, 75, align='center', width=375, height=200)
        drawLabel("My name's Pinky because I'm pink.", app.width - 350, 55, size=16, bold=True, align='center', fill='pink', font='caveat')
        drawLabel("Don't get too close to me!", app.width - 380, 85, size=16, bold=True, align='center', fill='pink', font='caveat')
        drawImage(app.url, app.width/2, app.height/2 - 75, align='center', width=450, height=250)
        drawImage(app.instructionsButton, app.width-50, app.height-50, align='center', width=175, height=100)
        app.pacman1.draw(app.width, app.pacman1.mouthAngle)
        app.pacman2.draw(app.width, app.pacman2.mouthAngle)
        
        drawImage(app.buttonImage, app.width/2 - 150, app.height/2 + 65, align='center', width=200, height=100)
        drawLabel('Regular Mode', app.width/2 - 150, app.height/2 + 65, 
                size=20, bold=True, align='center', fill='darkSlateGray', borderWidth=1, font = 'monospace')
        
        drawImage(app.buttonImage, app.width/2 + 150, app.height/2 + 65, align='center', width=200, height=100)
        drawLabel('Sandbox Mode', app.width/2 + 150, app.height/2 + 65, 
                size=20, bold=True, align='center', fill='darkSlateGray', borderWidth=1, font = 'monospace')
    
    # Draw out the classic pacman game
    elif app.regularMode == True:
        
        app.maze.draw()
        if app.gameOver:
            app.gamePacman.drawBlinking()
            if app.gamePacman.deathAnimationComplete:
                drawRect(0, 0, app.width, app.height, fill='black')
                drawImage(app.gameOverImage, app.width/2, app.height/2-50, align='center', width=1000, height=500)
                drawLabel(f'Your Score: {app.gamePacman.score}', app.width/2, app.height/2 + 50, size=30, bold=True, align='center', fill = 'white', border = 'yellow')
                drawImage(app.restartImage, app.width/2, app.height/2 + 150, align = 'center', width = 600, height = 45)
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
            if app.inky.returningToBase == False:
                app.inky.draw()
            else:
                app.inky.drawEyes()
            app.gamePacman.drawMovement(app.gamePacman.mouthAngle)

    # Draw out the sandbox mode
    elif app.sandBoxMode == True:
        app.sandBoxMaze.draw()
        if app.gameOver:
            app.gamePacman.drawBlinking()
            if app.gamePacman.deathAnimationComplete:
                drawRect(0, 0, app.width, app.height, fill='black')
                drawImage(app.gameOverImage, app.width/2, app.height/2-50, align='center', width=1000, height=500)
                drawLabel(f'Your Score: {app.gamePacman.score}', app.width/2, app.height/2 + 50, size=30, bold=True, align='center', fill = 'white', border = 'yellow')
                drawImage(app.restartImage, app.width/2, app.height/2 + 150, align = 'center', width = 600, height = 45)
        else:
            app.blinky.draw()
            app.clyde.draw()
            app.pinky.draw()
            app.inky.draw()
            if app.drawnPacMan:
                app.gamePacman.drawMovement(app.gamePacman.mouthAngle)
       
       # Draw out the inventory and the maze during sandbox mode
        if app.drawMode:
            drawRect(0, app.height - 50, 100, 45, fill = None, border = 'white', borderWidth = 5)
            drawLabel('Play', 50, app.height - 29, size=30, bold=True, align='center', fill = 'white', border = 'black', borderWidth = 1)
            for i in range(6):         
                if (i == 0 and app.drawWall) or (i == 1 and app.drawPacMan) or (i == 2 and app.drawPellet) or (i == 3 and app.drawPowerPellet) or (i == 5 and app.drawEraser):
                    borderColor = 'blue' 
                else:
                    borderColor = 'white'
                drawRect(225 + i * (60), app.height - 50, 50, 50, 
                        fill='gray', border=borderColor)
                
                if i == 0:  
                    drawRect(235 + i * 60, app.height - 40, 30, 30, fill='blue')
                elif i == 1:  
                    drawArc(250 + i * 60, app.height - 25, 30, 30, 45, 270, fill='yellow')
                elif i == 2:  
                    drawCircle(250 + i * 60, app.height - 25, 5, fill='white')
                elif i == 3:  
                    drawCircle(250 + i * 60, app.height - 25, 10, fill='white')
                elif i == 4:  
                    drawCircle(250 + i * 60, app.height - 25, 15, fill='red')
                    drawRect(235 + i * 60, app.height - 25, 30, 15, fill='red')
                elif i == 5:  
                    drawRect(235 + i * 60, app.height - 40, 30, 30, fill='pink')
                    drawLine(235 + i * 60, app.height - 40, 
                            265 + i * 60, app.height - 10, fill='red')
                    drawLine(265 + i * 60, app.height - 40, 
                            235 + i * 60, app.height - 10, fill='red')
            if app.drawPopUp:
                drawImage(app.popUpImage, app.width/2, app.height/2 - 20, align='center', width = 400, height = 200)
                drawLabel('Cannot erase ghost base!', app.width/2, app.height/2 - 20, size=20, align='center', fill = 'black', font = 'monospace')
            elif app.drawPopUp2:
                drawImage(app.popUpImage, app.width/2, app.height/2 - 20, align='center', width = 400, height = 200)
                drawLabel('Place down Pac-man!', app.width/2, app.height/2 - 20, size=20, align='center', fill = 'black', font = 'monospace')
            else:
                if app.drawWall:
                    drawRect(app.cx, app.cy, 30, 30, fill='blue', align = 'center')
                elif app.drawPacMan:
                    drawArc(app.cx, app.cy, 30, 30, 45, 270, fill='yellow')
                elif app.drawPellet:
                    drawCircle(app.cx, app.cy, 5, fill='white', align = 'center')
                elif app.drawPowerPellet:
                    drawCircle(app.cx, app.cy, 10, fill='white', align = 'center')
                elif app.drawEraser:
                    drawRect(app.cx - 15, app.cy - 15, 30, 30, fill='pink')
                    drawLine(app.cx - 15, app.cy - 15, app.cx + 15, app.cy + 15, fill='red')
                    drawLine(app.cx + 15, app.cy - 15, app.cx - 15, app.cy + 15, fill='red')
    elif app.instructions:
        drawImage(app.backArrowImage, 50, app.height - 50, align='center', width=100, height=100)
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
        if app.regularMode or (app.sandBoxMode and app.drawMode == False):
            app.gamePacman.update1()
            
            # Checks if PacMan has collided with any ghosts
            dist = (app.gamePacman.radius + app.blinky.radius)/2
            if distance(app.gamePacman.x, app.gamePacman.y, app.blinky.x, app.blinky.y) < dist and app.blinky.returningToBase == False: 
                if app.gamePacman.poweredUp == False:
                    app.gameOver = True
                    app.deathSound.play()
                else:
                    app.eatingGhostSound.play()
                    app.gamePacman.score += 200
                    app.blinky.returningToBase = True
     
            elif distance(app.gamePacman.x, app.gamePacman.y, app.clyde.x, app.clyde.y) < dist and app.clyde.returningToBase == False:
                if app.gamePacman.poweredUp == False:
                    app.gameOver = True
                    app.deathSound.play()
                else:
                    app.eatingGhostSound.play()
                    app.gamePacman.score += 200
                    app.clyde.returningToBase = True
            elif distance(app.gamePacman.x, app.gamePacman.y, app.pinky.x, app.pinky.y) < dist and app.pinky.returningToBase == False:
                if app.gamePacman.poweredUp == False:
                    app.gameOver = True
                    app.deathSound.play()
                else:
                    app.eatingGhostSound.play()
                    app.gamePacman.score += 200
                    app.pinky.returningToBase = True
            elif distance(app.gamePacman.x, app.gamePacman.y, app.inky.x, app.inky.y) < dist and app.inky.returningToBase == False:
                if app.gamePacman.poweredUp == False:
                    app.gameOver = True
                    app.deathSound.play()
                else:
                    app.eatingGhostSound.play()
                    app.gamePacman.score += 200
                    app.inky.returningToBase = True
            
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
                
                if app.inky.returningToBase:
                    app.inky.returnToBase()
                elif app.inky.inBase and app.counter > app.inkyLeave:
                    app.inky.moveOutBase()
                else:
                    if app.gamePacman.poweredUp:
                        app.inky.frighten()
                    else:
                        app.inky.turned = False
                        app.inky.chase(app.gamePacman.x, app.gamePacman.y, app.blinky.x, app.blinky.y)
        else:   
            # Loading screen Pacmans
            app.pacman1.update()
            app.pacman2.update()
    else:
        app.gamePacman.updateDeath()


def onKeyPress(app, key):
    # Move PacMan when he is still or moving
    if ((app.sandBoxMode == True and app.drawMode == False)or app.regularMode == True) and key in ['up', 'down', 'right', 'left']:
        app.gamePacman.still = False
        app.ghostStill = False
        app.gamePacman.nextDirection = key
    if app.gameOver and key == 'r':
        resetGame(app)
    
    # Controls for the inventory during sandbox mode
    if app.sandBoxMode:
        if key == '1' and app.drawMode:
            resetComponents(app)
            app.drawWall = True
        elif key == '2' and app.drawMode:
            resetComponents(app)
            app.drawPacMan = True
        elif key == '3' and app.drawMode:
            resetComponents(app)
            app.drawPellet = True
        elif key == '4' and app.drawMode:
            resetComponents(app)
            app.drawPowerPellet = True
        elif key == '6' and app.drawMode:
            resetComponents(app)
            app.drawEraser = True

def onMouseMove(app, mouseX, mouseY):

    # Illustrates the cursor during sandbox mode
    if app.drawMode:
        app.cx = mouseX 
        app.cy = mouseY 

def onMousePress(app, mouseX, mouseY):
    # Start the classic pacman game
    if mouseX >= app.width/2 - 250 and mouseX <= app.width/2 - 50 and mouseY >= app.height/2 + 15 and mouseY <= app.height/2 + 115 and app.start == False:
        app.regularMode = True
        app.start = True
        app.stepsPerSecond = 20
    # Start the sandbox mode
    elif mouseX >= app.width/2 + 50 and mouseX <= app.width/2 + 350 and mouseY >= app.height/2 + 15 and mouseY <= app.height/2 + 115 and app.start == False:
        app.sandBoxMode = True
        app.background = 'black'
        app.start = True
        app.stepsPerSecond = 20
        app.height = 850 # expanding the height to fit the hotbar
    # Draw out the maze during sandbox mode
    elif app.sandBoxMode and not app.drawPopUp:
        
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
            elif app.drawEraser:
                rows = range(8, 12)
                cols = range(7, 13)
                
                # Prevent user from erasing the ghost base
                if row not in rows or col not in cols:
                    app.sandBoxMaze.drawEraser(row, col)
                else:
                    app.drawPopUp = True
        elif mouseX >= 0 and mouseX <= 100 and mouseY >= app.height - 50 and mouseY <= app.height:
            if app.drawnPacMan == False:
                app.drawPopUp2 = True
            else:
                app.drawPopUp = True
                app.drawMode = False
                app.maze = app.sandBoxMaze
                app.height = 800

    # Go back to the main menu
    elif app.instructions:
        if mouseX >= 0 and mouseX <= 100 and mouseY >= app.height - 100 and mouseY <= app.height:
            app.instructions = False
            app.background = 'grey'
    
    # Close the pop up
    if (app.drawPopUp or app.drawPopUp2) and (mouseX >= 560 and mouseX <= 580) and (mouseY >= 310 and mouseY <= 330):
        app.drawPopUp = False
        app.drawPopUp2 = False
    
    # Go to the instructions page
    elif mouseX >= app.width-135 and mouseX <= app.width and mouseY >=app.height - 100 and mouseY <= app.height:
        app.instructions = True
        app.background = 'black'

def main():
    runApp()
    


main()