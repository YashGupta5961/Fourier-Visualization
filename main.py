import pygame
import numpy as np
import time
import math
import random

pygame.init()
pygame.font.init()

FONT = pygame.font.SysFont("comicsans", 30)
FONTL = pygame.font.SysFont("comicsans", 80)

WIN_WIDTH = 1200
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


# def convert():
#     pass

# def mySort(data):
#     res = list()
#     curr = [0, 0]
#     while(data):
#         closest = data[0]
#         for p in data:
#             closeDis = dist(closest, p)
#             currDis = dist(curr, p)
            
#             if(currDis < closeDis):
#                 closest = p

#         res.append(closest)
#         data.remove(closest)
#         curr = res[-1]
#     return res


# def dist(p1, p2):
#     dis = math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
#     if (dis == 0):
#         return 1000000
#     else:    
#         return dis

def intro(win, clock):
    baseA = 100
    baseF = 0
    epicycles = 1
    base = Func(0, 0, 0)
    base.centerX = 875
    base.centerY = 275 

    header = FONTL.render("Initialize fourier series:", 1, (255,255,255))

    starttext = FONT.render("Draw", 1, (255,255,255))
    startB = [400, 360, 100, 110]
    
    amptext = FONT.render("Amplitude", 1, (255,255,255))
    ampBP = [75, 150, 100, 50]
    ampBM = [75, 210, 100, 50]


    freqtext = FONT.render("Frequency", 1, (255,255,255))
    freqBP = [400, 150, 100, 50]
    freqBM = [400, 210, 100, 50]

    cyctext = FONT.render("Cycles", 1, (255,255,255))
    cycleBP = [75, 360, 100, 50]
    cycleBM = [75, 420, 100, 50]

    plustext = FONT.render("+", 1, (0,0,0))
    minustext = FONT.render("-", 1, (0,0,0))

    checktext = FONT.render('Δ', 1, (0,0,0))

    buttons = [startB, ampBP, ampBM, freqBP, freqBM, cycleBP, cycleBM]
    texts = [[header, (275, 20)], [starttext, (425, 330)], [amptext,(75, 120)] , [freqtext,(400, 120)], [cyctext,(95, 330)], [plustext, (118, 165)], [minustext, (120, 225)], [plustext, (118, 375)], [minustext, (120, 435)], [plustext, (443, 165)], [minustext, (445, 225)], [checktext, (445, 405)]]         

    t1 = time.time()
    intro = True
    while intro:
        clock.tick(120)
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse[0] < startB[0]+startB[2] and startB[0] < mouse[0] and mouse[1] < startB[1]+startB[3] and startB[1] < mouse[1]:
                    intro = False
                    break
                if mouse[0] < ampBP[0]+ampBP[2] and ampBP[0] < mouse[0] and mouse[1] < ampBP[1]+ampBP[3] and ampBP[1] < mouse[1]:
                    baseA += 1
                if mouse[0] < ampBM[0]+ampBM[2] and ampBM[0] < mouse[0] and mouse[1] < ampBM[1]+ampBM[3] and ampBM[1] < mouse[1]:
                    baseA -= 1
                if mouse[0] < freqBP[0]+freqBP[2] and freqBP[0] < mouse[0] and mouse[1] < freqBP[1]+freqBP[3] and freqBP[1] < mouse[1]:
                    baseF += 1
                if mouse[0] < freqBM[0]+freqBM[2] and freqBM[0] < mouse[0] and mouse[1] < freqBM[1]+freqBM[3] and freqBM[1] < mouse[1]:
                    baseF -= 1
                if mouse[0] < cycleBP[0]+cycleBP[2] and cycleBP[0] < mouse[0] and mouse[1] < cycleBP[1]+cycleBP[3] and cycleBP[1] < mouse[1]:
                    epicycles += 1
                if mouse[0] < cycleBM[0]+cycleBM[2] and cycleBM[0] < mouse[0] and mouse[1] < cycleBM[1]+cycleBM[3] and cycleBM[1] < mouse[1]:
                    epicycles -= 1
        
        base.radius = baseA
        base.omega = baseF

        base.rotate(1.8*(time.time() - t1))
        drawIntro(win, buttons, texts, base, baseA, baseF, epicycles)
    return baseA, baseF, epicycles
        

def drawIntro(win, buttons, texts, base, baseA, baseF, epicycles):
    win.fill((0,0,0))
    for b in buttons:
        pygame.draw.rect(win, (255,255,255), b)

    for t in texts:        
        win.blit(t[0], t[1]) 
    base.draw(win)
    ampVal = FONTL.render(str(baseA), 1, (255,255,255))
    win.blit(ampVal, (200, 180))
    freqVal = FONTL.render(str(baseF), 1, (255,255,255))
    win.blit(freqVal, (530, 180))
    cycVal = FONTL.render(str(epicycles), 1, (255,255,255))
    win.blit(cycVal, (200, 390))
    pygame.display.update()
        


def drawWindow(win, functions, res):
    pygame.draw.rect(win, (0,0,0), (0, 0, WIN_WIDTH, WIN_HEIGHT))
    for f in functions:
        f.draw(win)
    res.draw(win)
    pygame.draw.line(win, (255, 0, 0), (functions[-1].x, functions[-1].y), (500, functions[-1].y))
    pygame.display.update()

def main(win, clock, baseA, baseF, epicycles):
    run = True
    res = Output()
    base = Func(baseA, baseF, 0)
    functions = list()
    functions.append(base)
    
    if baseF < 0:
        start = baseF - 2
        step = -2
        end = (epicycles * step) + baseF
    elif baseF > 0:
        start = baseF + 2
        step = 2
        end = (epicycles * step) + baseF
    else:
        run = False
        return

    for x in range(start, end, step):
        functions.append(Func(baseA/abs(x), x, 0, functions[-1]))
    
    
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
baseA, baseF, epicycles = intro(myWin, myClock)
main(myWin, myClock, baseA, baseF, epicycles)

