import math


def minTimeToVisitAllPoints(points):

    prev = points[0]
    c = 0
    for i in range(1,len(points)):
        c += tricky_distanse(prev[0],prev[1],points[i][0],points[i][1])
        prev = points[i]
    return c

def tricky_distanse(x1,y1,x2,y2):
    x = abs(x1-x2)
    y = abs(y1-y2)
    c=0
    while x > 0 and y > 0:
        c += 1
        x -= 1
        y -= 1
    c = c + x + y
    return c

points = [[1,1],[3,4],[-1,0]]


print(minTimeToVisitAllPoints(points))
#%%
