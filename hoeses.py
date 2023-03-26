# Importing pygame module
import pygame
import random
import sys
import keyboard
from pygame.locals import *

Window = None
snowballs = []
snowball_amount = 500
moveMaxX = 1
moveMaxY = 3

class Colors:
    White = (255, 255, 255)
    Black = (0, 0, 0)
    Blue = (0, 50, 200)

class Window:
    def __init__(self):
        pygame.init()

        self.mainClock = pygame.time.Clock()
        self.Color = Colors.Black #background color
        self.Width = 600 #x
        self.Height = 600 #y
        self.window = pygame.display.set_mode((self.Width, self.Height))
        self.MousePosition = {"x" : 0,"y" : 0}

    def Render(self):
        self.window.fill(self.Color) #filling window with current color
        self.MousePosition = { #getting mouse position
            "x" : pygame.mouse.get_pos()[0],
            "y" : pygame.mouse.get_pos()[1]
        }

    def IsPositionOutOfBounds(self, x, y):
        if x > (self.Width - 10) or y > (self.Height - 10):
            return True

class snowball:
    global moveMaxX
    global moveMaxY

    def __init__(self):
        self.Position = {
            "x" : random.randint(1, (Window.Width - 1)),
            "y" : random.randint(1, (Window.Height * (Window.Height / 1000)))
        }
        self.Color = Colors.White
        self.CircleRadius = 4
        self.circle = None

    def Render(self):
        self.circle = pygame.draw.circle(Window.window, self.Color, [self.Position['x'], self.Position['y']], self.CircleRadius)

        #move
        movex = random.randint(0, moveMaxX)
        movey = random.randint(0, moveMaxY)

        self.Position['x'] -= movex
        self.Position['y'] += movey

#source: https://github.com/psuchta/autonomous_parking/blob/c9edbca020c8fa61bc9a06d222d4e2505810a1b2/cars/car.py#L31
def vec2_distance(point, second_point):
    return pygame.math.Vector2.distance_to(pygame.Vector2(point), pygame.Vector2(second_point))

def SnowBalling():
    global snowball_amount
    while True:
        Window.Render()

        while len(snowballs) < snowball_amount:
            snowballs.append(snowball())

        for ball in snowballs:
            ball.Render()
            if Window.IsPositionOutOfBounds(ball.Position['x'], ball.Position['y']):
                snowballs.remove(ball)
                del ball
                continue

            ''' NeEd To iNVeSTiGaTe
            for ball2 in snowballs:
                dist = vec2_distance(pygame.math.Vector2(ball.Position['x'], ball.Position['y']), pygame.math.Vector2(ball2.Position['x'], ball2.Position['y']))
                ##print(dist)
                if dist < 0.01:
                    snowballs.remove(ball)
                    del ball
                    ball2.CircleRadius += 5
                    break
            '''
            
        '''
        for ball in snowballs:
                    for ball2 in snowballs:
                        ball2.Render()

                        if Window.IsPositionOutOfBounds(ball2.Position['x'], ball2.Position['y']):
                            snowballs.remove(ball2)
                            del ball2
                        
                        dist = vec2_distance(pygame.math.Vector2(ball.Position['x'], ball.Position['y']), pygame.math.Vector2(ball2.Position['x'], ball2.Position['y']))
                        print(dist)
                        if dist < 0.01:
                            snowballs.remove(ball)
                            del ball
                            ball2.CircleRadius += 1
                            break
        '''
        
        global moveMaxX
        global moveMaxY

        #print all info
        print(f"Mouse Position:{Window.MousePosition}|Snow Balls:{len(snowballs)}|FPS:{Window.mainClock} moveMaxX:{moveMaxX}|moveMaxY:{moveMaxY}", end='\r')

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == K_UP:
                    snowball_amount += 10
                elif event.key == K_DOWN:
                    snowball_amount -= 10
                elif event.key == K_LEFT:
                    if not moveMaxX > 20:
                        moveMaxX += 1
                    if moveMaxY > 1:
                        moveMaxY -= 1
                elif event.key == K_RIGHT:
                    if not (moveMaxY > 20):
                        moveMaxY += 2
                    if not (moveMaxX > 20):
                        moveMaxX += 1
        
        pygame.display.update()
        Window.mainClock.tick(60)

if __name__ == "__main__":
    Window = Window()
    SnowBalling()
