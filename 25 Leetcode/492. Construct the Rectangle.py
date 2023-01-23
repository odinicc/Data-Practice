import math


def constructRectangle(area):
    diviers1 = []
    diviers2 = []
    for i in range(1,int(area**0.5)+1):
        if area%i == 0:
            diviers1.append(i)
            diviers2.append(int(area/i))
    return [diviers2[-1] ,diviers1[-1]]






area = 122122
print(constructRectangle(area))