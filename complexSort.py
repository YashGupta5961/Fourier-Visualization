
import numpy as np

# p0 = np.complex(0,0)

# def dist(p1, p2):
#     return np.sqrt((p2.real - p1.real)**2 + (p2.imag - p1.imag)**2)

# def swap(lst, pos1, pos2):
#     temp = lst[pos1]
#     lst[pos1] = lst[pos2]
#     lst[pos2] = temp
#     return

# def orientation(p1, p2, p3):
#     val = ((p2.imag - p1.imag) * (p3.real - p2.real)) - ((p2.real - p1.real) * (p3.imag - p2.imag))
#     if val < 0:
#         return 2
#     elif val > 0:
#         return 1
#     else:
#         return 0

# def compare(p1, p2):
#     orient = orientation(p0, p1, p2)
#     if orient == 0:
#         if(dist(p0, p2) >= dist(p0, p1)):
#             return -1
#         else:
#             return 1
#     else:
#         if orient == 2:
#             return -1
#         else:
#             return 1

# def mySort(points, length):
#     ymin = points[0].imag
#     min_ = 0
#     for i in range(length):
#         y = points[i].imag
#         if (y < ymin) or (y == ymin and points[i].real < points[min_].real):
#             ymin = points[i].imag
#             min_ = i
    
#     swap(points, 0, min_)
    
#     global p0 
#     p0 = points[0]

#     sorted = points[1:-1].sort(key = lambda x: compare(x, points(points.index(x)+1)))
#     sorted.insert(0, p0)

#     return sorted

# def mySort(data):
#     res = list()
#     curr = [-1000, -1000]
#     while data:
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
#     dis = np.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
#     if (dis == 0):
#         return 1000000
#     else:    
#         return dis