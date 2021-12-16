#pygame testing

import pygame

w = 500
h = 500
screen = pygame.display.set_mode((w, h))

background = (0, 0, 0)
screen.fill(background)

pygame.display.set_caption("pygame testing")

r = 100
g = 100
b = 100
x = 250
y = 250
length = 100
width = 100

pygame.draw.rect(screen, (r, g, b), (x, y, x, y))


for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit() 
