
import re

x = "Herb the sage eats sage, the herb"
print(" x = ", x)


def only_words(x):
    res = x.split()
    for i in range(len(res)):
        res[i] = re.sub('[,:;.]', '', res[i])
    return res

def palidrom(x):
    y = x.lower()
    res  = only_words(y)
    k = len(res)
    for i in range(k):
        if res[i] != res[k-i-1]:
            return False
    else:
        return True

print("only_words(x) = " , palidrom(x) )

