a = [] 
x = int(input("input  your age "))
a.append(x)

while x != 0:
    x = int(input("input  your age "))
    a.append(x)

for k in range(len(a)):
    if 0 < a[k] <= 2:
        a[k] = 0
    elif 2 < a[k] <= 12:
        a[k] = 12
    elif 65 < a[k]:
        a[k] = 18
    else:
        a[k] = 23
               
print(a)
print("sum(a) =  ", sum(a))
    
