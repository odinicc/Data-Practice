import math

x = 184

def prime(x):
    d = []
    for i in range(2,round(math.sqrt(x))+1):
        if x%i == 0:
            d.append(i)
    if len(d) == 0:
        return True
    else:
        return False

def nextprime(x):
    k = x
    while prime(k) != True:
        k += 1
        #print(k)
    return k


print("next prime" , nextprime(x))


