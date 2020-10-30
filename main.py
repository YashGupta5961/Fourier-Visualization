import pygame
import numpy as np
import time
import math
import random

pygame.init()

WIN_WIDTH = 1500
WIN_HEIGHT = 500

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
        pygame.draw.circle(win, (255,0,0), (self.x, self.y), 3, 0)

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
        for p in self.points:
            pygame.draw.circle(win, (0,0,255), (p[0], p[1]), 1, 0)


def convert():
    pass

def mySort(data):
    res = list()
    curr = [0, 0]
    while(data):
        closest = data[0]
        for p in data:
            closeDis = dist(closest, p)
            currDis = dist(curr, p)
            
            if(currDis < closeDis):
                closest = p

        res.append(closest)
        data.remove(closest)
        curr = res[-1]
    return res



def dist(p1, p2):
    dis = math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
    if (dis == 0):
        return 1000000
    else:    
        return dis

def drawWindow(win, functions, res):
    pygame.draw.rect(win, (0,0,0), (0, 0, WIN_WIDTH, WIN_HEIGHT))
    for f in functions:
        f.draw(win)
    res.draw(win)
    pygame.draw.line(win, (255, 0, 0), (functions[-1].x, functions[-1].y), (500, functions[-1].y))
    pygame.display.update()

def main():
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    run = True
    clock = pygame.time.Clock()
    res = Output()
    base = Func(100, -2, 0)
    functions = list()
    functions.append(base)
    
    for x in range(4, 50, 2):
        functions.append(Func(100/x, -x, 0, functions[-1]))
    
    
    t1 = time.time()
    while(run):
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        base.rotate(time.time() - t1)
        for i in range(1, len(functions)):
            functions[i].rotate(time.time() - t1, functions[i-1])

        

        res.update([500, functions[-1].y])

        drawWindow(win, functions, res)

    pygame.quit()
    quit()

main()

# inp = [[7,2], [11, 12], [3,2], [5, 10], [8, 6]]
# print(inp)
# res = mySort(inp)
# print(res)