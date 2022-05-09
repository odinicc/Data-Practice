import random
import pprint
import sys

#input = open('1.txt', 'r') //расскомментировать решая задачу локально
# input = sys.stdin //расскомментировать при сдаче задачи в системе


S = []
n = int(input.readline())
for i in range(1,n+1):
  x,y = map(int, input.readline().split())
  S.append([x,y])


back_pack = 20
n = 3
goods = []

for i in range(10):
    c = []
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    c.append(a)
    c.append(b)
    goods.append(c)

n , back_pack = map(int, input().split())




for i in range(len(goods)):

    d = round((goods[i][0])/(goods[i][1]),3)
    goods[i].append(d)

goods.sort(reverse=True,key=lambda elem: elem[2])

free_back_pack = back_pack
overal_back_pack_cost = 0
for i in range(len(goods)):
    if goods[i][1]< free_back_pack:
        overal_back_pack_cost += goods[i][0]
        free_back_pack -= goods[i][1]
    else:
        overal_back_pack_cost += round(goods[i][2]*free_back_pack,3)

print(overal_back_pack_cost)