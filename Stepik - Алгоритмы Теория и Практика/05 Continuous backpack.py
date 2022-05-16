import random
import sys

#for local solution
inf = open('1.txt', 'r')

#for system solution
# inf = sys.stdin

Lines = inf.readlines()

First_Line = Lines[0]
words = First_Line.split(" ")
back_pack = int(words[1].replace('\n', ''))
n = int(words[0])
Lines.pop(0)

goods = []

for Line in Lines:
    words = Line.split(" ")
    price = int(words[0])
    weight = int(words[1].replace('\n', ''))
    goods.append([price,weight])


for i in range(len(goods)):

    d = round((goods[i][0])/(goods[i][1]),10)
    goods[i].append(d)

goods.sort(reverse=True,key=lambda elem: elem[2])

free_back_pack = back_pack
overal_back_pack_cost = 0

for i in range(len(goods)):
    if goods[i][1]< free_back_pack:
        overal_back_pack_cost += goods[i][0]
        free_back_pack -= goods[i][1]
    else:
        overal_back_pack_cost += round(goods[i][2]*free_back_pack,10)
        free_back_pack = 0

print(round(overal_back_pack_cost,3))