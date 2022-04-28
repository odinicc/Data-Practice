import math
x = 49

def perfect(n):
    l = []
    for i in range(1,n):
        #print(i)
        if n%i == 0:
            l.append(i)
    print(l)
    if sum(l) == n:
        return True
    else:
        return False
            

def isprime(n):
    for i in range(2,round(math.sqrt(n)+1)):
        if n%i == 0:
            return False
    return True
            

#print(isprime(13))
print(perfect(28))

