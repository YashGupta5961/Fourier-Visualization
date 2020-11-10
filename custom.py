import pygame
import time
import numpy as np

WIN_WIDTH = 1200
WIN_HEIGHT = 500

pygame.init()



class Func:
    def __init__(self, r, w, phase, prev=None):
        if prev != None:
            self.centerX = prev.x
            self.centerY = prev.y
        else:
            self.centerX = 200
            self.centerY = 250
        self.radius = int(r)
        self.omega = w
        self.phase = phase
        self.x = int(self.centerX + (r * np.cos(phase)))
        self.y = int(self.centerY + (r * np.sin(phase)))

    def rotate(self, time, prev=None):
        if prev != None:
            self.centerX = prev.x
            self.centerY = prev.y
        self.x = int(self.centerX + (self.radius * np.cos((self.omega * time) + self.phase)))
        self.y = int(self.centerY + (self.radius * np.sin((self.omega * time) + self.phase)))


    def draw(self, win):
        pygame.draw.circle(win, (255,255,255), (self.centerX, self.centerY), self.radius, 1)
        # pygame.draw.circle(win, (255,0,0), (self.x, self.y), 3, 0)
        pygame.draw.line(win, (255,255,255,127), (self.centerX, self.centerY), (self.x, self.y), 1)


def drawWindow(win, functions, res):
    pygame.draw.rect(win, (0,0,0), (0, 0, WIN_WIDTH, WIN_HEIGHT))
    for f in functions:
        f.draw(win)
    res.draw(win)
    pygame.draw.line(win, (255, 0, 0), (functions[-1].x, functions[-1].y), (500, functions[-1].y))
    pygame.display.update()

class Output:
    def __init__(self):
        self.points = list()
    
    def update(self, point):
        for p in self.points:
            p[0] += 1
        self.points.append(point)
        if self.points[0][0] > WIN_WIDTH - 100:
            self.points.pop(0)
    
    def draw(self, win):
        if(len(self.points) > 1):
            pygame.draw.lines(win, (0,0,255), False, self.points)



def main(win, clock):
    run = True
    res = Output()
    base = Func(100, -2, 0)
    functions = [base]
    functions.append(Func(100, 2, np.pi, functions[-1]))

    
    t1 = time.time()
    while(run):
        clock.tick(120)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        t2 = 1.8*(time.time() - t1)
        base.rotate(t2)
        for i in range(1, len(functions)):
            functions[i].rotate(t2, functions[i-1])

        

        res.update([500, functions[-1].y])

        drawWindow(win, functions, res)

    pygame.quit()
    quit()

myWin = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
myClock = pygame.time.Clock()
main(myWin, myClock)
