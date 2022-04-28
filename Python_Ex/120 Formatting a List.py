
import re

x = "herb apples oranges  lemons grapes"
res = x.split()
print(" x = ", x)
print(" res= ", res)


def joy(res):
    st =""
    k = len(res)
    for i in range(k):
        if i < (k-2):
            st = st + res[i] + ", "
        elif i == k-2:
            st = st + res[i] +" and "
        else:
            st = st + res[i]

    return st

print(joy(res))




