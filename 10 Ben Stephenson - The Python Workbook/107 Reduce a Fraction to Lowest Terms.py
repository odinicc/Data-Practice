import math

x = 84
y = 160
xx = []
yy = []

for k in range(2,x+1):
    if x%k == 0:
        xx.append(k)

for i in range(2,y+1):
    if y%i == 0:
        yy.append(i)

print(xx)
print(yy)

q = len(yy)-1
while q>=0:
    print(yy[q])
    print(xx.count(yy[q]))
    print("  ")
    if xx.count(yy[q]) > 0:
        break
    q -= 1

print(yy[q])
print( int(x/yy[q]), "/" , int(y/yy[q]))


               
