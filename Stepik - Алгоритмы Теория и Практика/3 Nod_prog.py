import random
from recviz import recviz

def check(gcd, n_iter):
    for i in range(n_iter):
        c = random.randint(0,1024)
        a = c * random.randint(0,128)
        b = c * random.randint(0,128)
        assert gcd(a, a) == gcd(a, 0)==a
        assert gcd(b, b) == gcd(b, 0)==b
        assert gcd(a, 1) == gcd(b, 1)==1
        d = gcd(a,b)
        assert a%d == b%d == 0

n_iter = 100

def gcd1(a,b):
    for d in reversed (range(max(a,b) + 1)):
        if d==0 or a%d == b%d ==0:
            return d
@recviz
def gcd2(a,b):
    while a and b:
        if a >= b:
            a %= b
        else:
            b %= a
    return max(a,b)

def gcd4(a, b):
    if a==0 or b==0:
        return max(a,b)
    return gcd4(b%a,a)

print(gcd1(0,0))

#print(check(gcd1,n_iter))
#print(check(gcd2,n_iter))

print(gcd2(24,9))
print(gcd4(24,9))