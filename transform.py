import pygame
import numpy as np
import time
import cv2
from matplotlib import pyplot as plt
import complexSort

pygame.init()
pygame.font.init()

FONT = pygame.font.SysFont("comicsans", 30)
FONTL = pygame.font.SysFont("comicsans", 80)

WIN_WIDTH = 1800
WIN_HEIGHT = 1000

class Func:
    def __init__(self, r, w, phase, prev=None):
        if prev != None:
            self.centerX = int(prev.x)
            self.centerY = int(prev.y)
        else:
            self.centerX = int(500)
            self.centerY = int(500)
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
        pygame.draw.circle(win, (255,255,255,10), (self.centerX, self.centerY), self.radius, 1)
        pygame.draw.line(win, (255,255,255,0.1), (self.centerX, self.centerY), (self.x, self.y), 1)

class Output:
    def __init__(self):
        self.points = list()
        self.flag = False

    def update(self, point):
        self.points.append(point)
        if len(self.points) > 1000:
            self.points.pop(0)
    
    def draw(self, win):
        if len(self.points) > 1:
            pygame.draw.lines(win, (0,0,255), False, self.points)
        # else:
        #     for p in self.points:
        #         pygame.draw.circle(win, (0,0,255), (p[0], p[1]), 1, 0)

def outline(image):
    img = cv2.imread(image)
    bw = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret,thresh1 = cv2.threshold(bw,127,255,cv2.THRESH_BINARY)
    thresh = cv2.adaptiveThreshold(thresh1, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    
    # cv2.imshow('test',thresh)
    # cv2.waitKey(0)

    kernel = np.ones((3,3),np.uint8)
    erosion = cv2.erode(thresh, kernel,iterations = 1)
    opening = cv2.morphologyEx(erosion, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
    

    contours, hierarchy = cv2.findContours(closing,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) 
    
    areas = list()
    for contour in contours:
        ar = cv2.contourArea(contour)
        areas.append(ar)

    max_area = max(areas)
    max_area_index = areas.index(max_area)

    cnt = contours[max_area_index]
    blank = np.zeros((img.shape[0:2]), np.uint8)

    
    cv2.drawContours(blank, [cnt], 0, (255, 255, 255), 1, maxLevel = 0)
    # cv2.imshow('test',blank)
    # cv2.waitKey(0)
    return blank

# def convert(comp):
#     amp = (comp.real**2 + comp.imag**2)**0.5
#     phase = np.arctan2(comp.imag,comp.real)
#     return amp, phase

def fft(x):
    N = len(x)
    X = [None]*N
    for k in range(N):
        sigma = np.complex(0,0)
        for n in range(N):
            phi = np.pi * 2 * n * k / N
            c = np.complex(np.cos(phi), -1*np.sin(phi))
            sigma += (x[n]*c)
        sigma /= N
        freq = k
        amp = np.sqrt(sigma.real*sigma.real + sigma.imag*sigma.imag)
        phase = np.arctan2(sigma.imag,sigma.real)
        X[k] = [amp, freq, phase, sigma]
    return X

def preprocess(image):
    img = outline(image)
    y, x = np.nonzero(img)
    
    inp = list()
    for i in range(len(x)):
        inp.append(np.complex(x[i]-img.shape[1]/2, y[i]-img.shape[0]/2))
    
    inp = complexSort.mySort(inp)

    skip = int(len(inp)/200)
    inp = inp[0::skip]

    inp = complexSort.mySort(inp)

    out = fft(inp)

    X = [x.real for x in inp]
    Y = [-1*x.imag for x in inp]

    plt.scatter(X,Y, color='red')
    plt.show()

    out.sort(key = lambda x: x[0])
    out.reverse()

    return out

def generateEpicycle(out):
    functions = list()
    count = 0
    for idx, func in enumerate(out):
        count += 1
        if(func[0] < 1):
            break
        if idx == 0:
            functions.append(Func(func[0], func[1], func[2]))
        else:
            functions.append(Func(func[0], func[1], func[2], functions[idx-1]))

    return functions

def drawWindow(win, functions, res):
    pygame.draw.rect(win, (0,0,0), (0, 0, WIN_WIDTH, WIN_HEIGHT))
    for f in functions:
        f.draw(win)
    res.draw(win)
    pygame.draw.line(win, (255, 0, 0), (functions[-1].x, functions[-1].y), (functions[-1].x + 800, functions[-1].y))
    pygame.display.update()



def main(image):
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()


    out = preprocess(image)
    functions = generateEpicycle(out)

    base = functions[0]
    res = Output()

    count = len(out) * 1
    t1 = 0
    dt = 2 * np.pi / count
    run = True
    while(run):
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        t1 += dt
        base.rotate(t1)
        for i in range(1, len(functions)):
            functions[i].rotate(t1, functions[i-1])

        if count >= 0:
            res.update([functions[-1].x + 800, functions[-1].y])
            # if count == 1:
            #     res.flag = True
            #     res.points = complexSort.mySort(res.points)

        drawWindow(win, functions, res)
        count-=1
        

    pygame.quit()
    quit()


main("test3.png")
# preprocess("test.png")

