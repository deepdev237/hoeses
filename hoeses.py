# Importing pygame module
import pygame
from pygame.locals import *

white = (255, 255, 255)
black = (0, 0, 0)

# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()
 
# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((600, 600))
 
# Fill the scree with white color
window.fill(black)

Pos = (50, 10)

Positions = [
    Pos
]

for x in range(1000):
    Pos = (Pos[0] + 20, Pos[1] + 10)
    Positions.append(Pos)
    print(Pos)

while True:
    pygame.display.update()

    for x in Positions:
        Position[x] = (Position[x][0] - 20, Position[x][1] - 10)
        pygame.draw.circle(window, white, x, 5)
        print(x)
        

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    
