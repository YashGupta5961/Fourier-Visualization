import random
import numpy as np
from matplotlib import pyplot as plt
from sklearn.neighbors import KDTree


def dist(p1, p2):
    return np.sqrt((p2.real - p1.real)**2 + (p2.imag - p1.imag)**2)

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



def mySort(data):
    # p0 = np.complex(0,0)
    res = list()
    curr = data.pop()
    res.append(curr)
    # currbest = curr
    while data:
        data.sort(key = lambda x : dist(curr, x))
        # for x in data:
        #     if compare(p0, curr, x):
        #         currbest = x
        #         break
        #     if len(data) == 1:
        #         currbest = data[0]
        currbest = data[0]
        res.append(currbest)
        data.remove(currbest)
        curr = res[-1]
        # p0 = res[-2]
    return res


    



# def dist(p1, p2):
#     dis = np.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
#     if (dis == 0):
#         return 1000000
#     else:    
#         return dis

# numbers = []
# theta = list(np.linspace(0, 2*np.pi, 20))
# random.shuffle(theta)
# print(type(theta))
# for i in theta:
#     r = 100
#     numbers.append(np.complex(int(r*np.cos(i)), int(r*np.sin(i))))

# print(numbers)
# numbers = [(-67-73j), (100+0j), (78-61j), (-8-99j), (78+61j), (-8+99j), (-98+16j), (-98-16j), (54-83j), (100+0j), (54+83j), (-87+47j), (94+32j), (24+96j), (-87-47j), (-40+91j), (-67+73j), (24-96j), (-40-91j), (94-32j)]

# numbers = [(9+6j), (43-18j), (50-37j), (-49-46j), (43+46j), (20+45j), (40+25j), (-27-10j), (-38+25j), (29+23j), (28-14j), (12+46j), (-40-26j), (-16-23j), (21-23j), (-31+30j), (-15+14j), (1+2j), (21-22j), (-29+18j)]

# X = [x.real for x in numbers]
# Y = [x.imag for x in numbers]
# plt.scatter(X,Y, color='red')
# for i, txt in enumerate(X):
#     plt.annotate(i, (X[i], Y[i]))
# plt.show()

# numbers = mySort(numbers)

# X = [x.real for x in numbers]
# Y = [x.imag for x in numbers]
# plt.scatter(X,Y, color='red')
# for i, txt in enumerate(X):
#     plt.annotate(i, (X[i], Y[i]))
# plt.show()