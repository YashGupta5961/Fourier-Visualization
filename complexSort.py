import random
import numpy as np
from matplotlib import pyplot as plt
from sklearn.neighbors import KDTree
import math
import time


# def swap(lst, pos1, pos2):
#     temp = lst[pos1]
#     lst[pos1] = lst[pos2]
#     lst[pos2] = temp
#     return

def orientation(p1, p2, p3):
    val = ((p2.imag - p1.imag) * (p3.real - p2.real)) - ((p2.real - p1.real) * (p3.imag - p2.imag))
    if val < 0:
        return 2
    elif val > 0:
        return 1
    else:
        return 0

def compare(p0, p1, p2):
    orient = orientation(p0, p1, p2)
    if orient == 0:
        if(dist(p0, p2) >= dist(p0, p1)):
            return False
        else:
            return True
    else:
        if orient == 2:
            return False
        else:
            return True

  


def dist(p1, p2):
    return ((p2.real - p1.real)**2 + (p2.imag - p1.imag)**2)

# Time complexity: n^2*log(n)
def mySort(data):
    res = list()
    curr = data.pop()
    res.append(curr)
    while data:
        data.sort(key = lambda x : dist(curr, x))
        currbest = data[0]
        res.append(currbest)
        data.remove(currbest)
        curr = res[-1]
    return res

# Time complexity: nlog(n). Doesnt work well as it sorts using polar angle
def mySort2(data):
    
    # compute centroid
    cent = np.complex(sum([p.real for p in data])/len(data),sum([p.imag for p in data])/len(data))
    
    # sort by polar angle
    data.sort(key = lambda p: math.atan2(p.imag-cent.imag, p.real-cent.real))

    return data

def minDis(p, data):
    # data.remove(p)
    currBest = data[0]
    for x in data:
        if(dist(p, currBest) > dist(p, x)):
            currBest = x
    return currBest      

# Time complexity: n^2
def mySort3(data):
    res = list()
    curr = data.pop()
    res.append(curr)
    while data:
        currbest = min(data, key=(lambda p: dist(curr,p)))
        res.append(currbest)
        data.remove(currbest)
        curr = res[-1]
    return res


# TESTS:

# numbers1 = list()
# numbers2 = list()
# for i in range(20000):
#     num = np.complex(random.randint(-1000, 1000), random.randint(-1000, 1000))
#     numbers1.append(num)
#     numbers2.append(num)

# start = time.time()
# numbers = mySort(numbers1)
# print("mySort = " + str(time.time() - start))

# start = time.time()
# numbers2 = mySort3(numbers2)
# print("mySort3 = " + str(time.time() - start))


# numbers = [(-67-73j), (100+0j), (78-61j), (-8-99j), (78+61j), (-8+99j), (-98+16j), (-98-16j), (54-83j), (100+0j), (54+83j), (-87+47j), (94+32j), (24+96j), (-87-47j), (-40+91j), (-67+73j), (24-96j), (-40-91j), (94-32j)]
# numbers = [(9+6j), (43-18j), (50-37j), (-49-46j), (43+46j), (20+45j), (40+25j), (-27-10j), (-38+25j), (29+23j), (28-14j), (12+46j), (-40-26j), (-16-23j), (21-23j), (-31+30j), (-15+14j), (1+2j), (21-22j), (-29+18j)]


# X = [x.real for x in numbers]
# Y = [x.imag for x in numbers]

# # dataReal = np.stack((X, Y), axis=1)

# plt.scatter(X,Y, color='red')
# for i, txt in enumerate(X):
#     plt.annotate(i, (X[i], Y[i]))
# plt.show()

# numbers = mySort3(numbers)

# X = [x.real for x in numbers]
# Y = [x.imag for x in numbers]
# plt.scatter(X,Y, color='red')
# for i, txt in enumerate(X):
#     plt.annotate(i, (X[i], Y[i]))
# plt.show()