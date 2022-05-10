import random
import sys

#for local solution
inf = open('1.txt', 'r')

#for system solution
# inf = sys.stdin

Lines = inf.readlines()

Lines.pop(0)

segments = []

for Line in Lines:
    words = Line.split(" ")
    price = int(words[0])
    weight = int(words[1].replace('\n', ''))
    segments.append([price, weight])

segments.sort(key=lambda elem: elem[1])




right_side = -1
points = []

for seg in segments:
    if seg[0] > right_side:
        points.append(seg[1])
        right_side = seg[1]


print(len(points))
print(*points)