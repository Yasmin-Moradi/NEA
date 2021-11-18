#start of program
#importing the module 'pygame' which will allow me to use aspects of it to create a game
import pygame

pygame.init()
#creating variable in order to set these for the user environment
w = 500
h = 500
screen = pygame.display.set_mode(size = (w, h))
fullscreen = True

def text_writing(colour, message, size, point):
    #when called, it will show text on screen
    print("placehold")
 

def main():
    #write rest of the code here
    print("placeholder for code")

class beatInput(self):
    #create blocks for inputs here
    print("placeholder 2)")

class Arrow(self):
    #create arrow inputs from user here
    #also create visible indicator inputs with pygame
    print("placeholder for code 3")

userName = str(input("Please enter your name: "))
if userName != str(userName):
    print("Sorry, your input was not valid")
    userName = str(input("Please enter your name: "))

#temporary choice offer
options = int(input("Type 1 to play, 2 for the tutorial, and 3 to quit"))
if options == 1:
    main()
if options == 2:
    tutorial()
if options == 3:
    quit()
else:
    print("Sorry, that input was not recognised")
    options = int(input("Type 1 to play, 2 for the tutorial, and 3 to quit"))
