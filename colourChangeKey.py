import pygame
import time
import random
#create object
#reacts to key press
#also changes at constant intervals
#reacts to key press

w = 500
h = 500
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("NEA rhythm game")
fullscreen = True


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
