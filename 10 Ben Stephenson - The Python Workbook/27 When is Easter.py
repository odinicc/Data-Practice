import math

yy = input("Enter a: ")
y = int(yy) 
a = y%19
print("a=", a)
b = y//100
print("b=", b)
c = y%100
print("c=", c)
d = y//4
print("d=", d)
e = y%4
print("e=", e)
f = (b+8)//25
print("f=", f)
g = (b-f+1)//3
print("g=", g)
h = (19*a + b - d - g + 15)%30
print("h=", h)
i = c//4
print("i=", i)
k = c%4
print("k=", k)
l = (32 + 2*e + 2*i - h - k)%7
print("l=", l)
m = (a + 11*h + 22*l)//451
print("m=", m)
month = (h + l - 7*m + 114) // 31
print("month=", month)
day = (h + l - 7*m + 114) % 31
print("day=", day)



