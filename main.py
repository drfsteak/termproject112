from cmu_graphics import *
from mediapipeDemo import HandTracker


def startPacMans(app):
    app.pacman1X = 0
    app.pacman2X = app.width
    app.pacman1Y = app.height/4
    app.pacman2Y = 3*app.height/4
    app.pacmanRadius = 100
    app.mouthAngle = 90
    app.closing = True


def onAppStart(app):
    app.handTracker = HandTracker()
    app.background = 'grey'
    app.width = 800
    app.height = 800
    startPacMans(app)
    app.url = '/Users/davidli/termproject112/images/download-removebg-preview (1).jpg'
    app.start = False
    app.regularMode = False
    app.aiMode = False
    app.stepsPerSecond = 35
    app.gameOver = False
    app.sound = Sound('https://eta.vgmtreasurechest.com/soundtracks/pac-man-game-sound-effects/gmiffyvl/Intro.mp3')





def redrawAll(app):
    # draw the title and instructions
    if app.gameOver == False:
        app.sound.play()
    if app.start == False:
        drawImage(app.url, app.width/2, app.height/2 - 100, align = 'center', width = 450, height = 200)
        startAngle = app.mouthAngle/2
        sweepAngle = 360 - app.mouthAngle
        drawArc(app.pacman1X, app.pacman1Y, app.pacmanRadius, app.pacmanRadius, startAngle, sweepAngle, fill = 'yellow', border = 'black')
        drawArc(app.pacman2X, app.pacman2Y, app.pacmanRadius, app.pacmanRadius, startAngle + 180, sweepAngle, fill = 'yellow', border = 'black')
        drawRect(app.width/2 - 250 , app.height/2 + 15, 200, 100, fill = None, border = 'blue', borderWidth = 5)
        drawLabel('Regular Mode', app.width/2 - 150, app.height/2 + 65, size = 20, bold = True, align = 'center')
        drawRect(app.width/2 + 50 , app.height/2 + 15, 200, 100, fill = None, border = 'blue', borderWidth = 5)
        drawLabel('AI Mode', app.width/2 + 150, app.height/2 + 65, size = 20, bold = True, align = 'center')

        if app.pacman1X + app.pacmanRadius > app.width:
            pixelsBeyondRightEdgeOfCanvas = app.pacman1X + app.pacmanRadius - app.width
            cx = -app.pacmanRadius + pixelsBeyondRightEdgeOfCanvas
            drawArc(cx, app.pacman1Y, app.pacmanRadius, app.pacmanRadius, startAngle, sweepAngle, fill = 'yellow', border = 'black')
        
        if app.pacman2X - app.pacmanRadius < 0:
            pixelsBeyondLeftEdgeOfCanvas = app.pacman2X - app.pacmanRadius
            cx = app.width + app.pacmanRadius - pixelsBeyondLeftEdgeOfCanvas
            drawArc(cx, app.pacman2Y, app.pacmanRadius, app.pacmanRadius, startAngle + 180, sweepAngle, fill = 'yellow', border = 'black')
    
    if app.aiMode == True:
        print("AI Mode is active")
        direction = app.handTracker.current_direction
        print(f"Current direction: {direction}")
        if direction:
            drawLabel(f"Direction: {direction}", 
                     app.width/2, 
                     app.height/2, 
                     size=30,
                     bold=True,
                     fill='yellow')
def onStep(app):
    direction = app.handTracker.update()
    if app.closing:
        app.mouthAngle -= 10
        if app.mouthAngle == 0:
            app.closing = False
    else:
        app.mouthAngle += 10
        if app.mouthAngle == 90:
            app.closing = True
    app.pacman1X += 10
    if app.pacman1X - app.pacmanRadius > app.width:
        pixelsBeyondRightEdgeOfCanvas = app.pacman1X + app.pacmanRadius - app.width
        app.pacman1X = -app.pacmanRadius + pixelsBeyondRightEdgeOfCanvas
    
    app.pacman2X -= 10
    if app.pacman2X + app.pacmanRadius < 0:
        pixelsBeyondLeftEdgeOfCanvas = app.pacman2X + app.pacmanRadius
        app.pacman2X = app.width + app.pacmanRadius - pixelsBeyondLeftEdgeOfCanvas

        


def onKeyPress(key):
    if key == 'escape':
        pass
    if key == 'up':
        pass
    elif key == 'down':
        pass
    elif key == 'right':
        pass
    elif key == 'left':
        pass
    

def onMousePress(app, mouseX, mouseY):
    if mouseX >= app.width/2 - 150 and mouseX <= app.width/2 + 150 and mouseY >= app.height/2 + 15 and mouseY <= app.height/2 + 115:
        app.regularMode = True
        app.start = True
    elif mouseX >= app.width/2 + 150 and mouseX <= app.width/2 + 350 and mouseY >= app.height/2 + 15 and mouseY <= app.height/2 + 115:
        app.aiMode = True
        app.start = True
    

def main():
    runApp()
    


main()