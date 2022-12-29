import math


def fizzBuzz(n):
    arr= []
    for i in range(1,n+1):
        arr.append(i)
    arr = [trans(x) for x in arr]
    return arr

def trans(x):
    x = int(x)
    if x % 3 == 0 and  x % 5 == 0:
        return 'FizzBuzz'
    elif x % 3 == 0:
        return 'Fizz'
    elif x % 5 == 0:
        return 'Buzz'
    else:
        return str(x)

n = 0
print(fizzBuzz(n))