#start of program
#importing the module 'pygame' which will allow me to use aspects of it to create a game
#time and random will be used in order to be used for the funcitonality of the aspects of the game
import pygame
import time
import random

pygame.init()
#creating variable in order to set these for the user environment
w = 500
h = 500

screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("NEA rhythm game")
fullscreen = True

#by making run = true, this checks that the program is running
#when run = false, this will trigger the endGame() function
run = True
while run:
    pygame.time.delay(250)
    
    #pygame's inbuilt feature of finding out when there is a key press event will help
    #this variable will be used to check when the event of a key being pressed is active
    #this will trigger a response onscreen
    keys = pygame.key.get_pressed()
    r = 0
    g = 0
    b = 0
    x = 250
    y = 250

    #pygame.draw.[shape]([location], [rgb], [x, y, width, height])

    pygame.draw.rect(screen, (r, g, b), (x, y, x, y))

    start = time.time()

    time.sleep(5)
    if keys[pygame.K_UP]:
        r += 2
        #change R value
    if keys[pygame.K_LEFT]:
        #change G value
        g += 2
    if keys[pygame.K_RIGHT]:
        #change B value
        b += 2
#have a variable that counts time and one that checks every 5 seconds
#every 5 seconds when it checks and then resets to white
        
    end = time.time()
    print("start:", start)
    print("end:", end)
    totalTime = end - start
    print("totalTime:", totalTime)

    if totalTime < 6 and totalTime > 4:
        pygame.draw.rect(screen, (50, 50, 50), (x, y, x, y))

    pygame.draw.rect(screen, (r, g, b), (x, y, x, y))


#if looking for specific version:
#for microseconds, use datetime.time()
#(for constant update of background, need set colour
screen.fill(255, 255, 255)

#pygame.draw.[shape]([location], [rgb], [x, y, width, height])
pygame.draw.rect(screen, (83, 71, 98), (x, y, x, y))

#need to do constant update so it doesnt leave trail
pygame.display.update()

def text_writing(colour, message, size, point):
    #when called, it will show text on screen
    print("placehold")

def runTutorial():
    #code for running the tutorial, small testing area, shows all functionalities, used as integrated environment
    print("placeholderB")

def endGame(run):
    #code for quitting, referenced in user choice
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            run = False
    pygame.quit()

def runGame():
    #write rest of the code here for contents of game
    print("placeholder for code")

def calculatePoints():
    #will reference class Arrow, to be referenced in runGame
    print("Placeholder")

class beatInput(self, up, down, left, right):
    #create blocks for inputs here
    self.inputUp = up
    self.inputDown = down
    self.inputLeft = left
    self.inputRight = right

class Arrow(self):
    #create arrow inputs from user here
    #also create visible indicator inputs with pygame
    print("placeholder for code 3")


def menuScreen():
    #temporary choice offer, would preferably like to display this on the screen and have the user select the options with a mouse
    options = int(input("Type 1 to play, 2 for the tutorial, and 3 to quit"))
    if options == 1:
        runGame()
    if options == 2:
        runTutorial()
    if options == 3:
        endGame()
    else:
        print("Sorry, that input was not recognised")
        options = int(input("Type 1 to play, 2 for the tutorial, and 3 to quit"))

userName = str(input("Please enter your name: "))
if userName != str(userName):
    print("Sorry, your input was not valid")
    userName = str(input("Please enter your name: "))