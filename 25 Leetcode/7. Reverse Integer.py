import math

#def twoSum(self, nums, target):
def reverse(x):
    if x == 0:
        return 0
    x = list(str(x))
    ll = len(x)
    print(x)
    for m in range(len(x)-1,-1,-1):
        if x[m] == '0':
            ll -= 1
        else:
            break

    x = x[0:ll]
    x = x[::-1]
    print(x)


    y = ''.join(x)
    return y



x = 1
print(reverse(x))


