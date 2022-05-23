
import re

x = "Contractions include: don’t, isn’t, and wouldn’t."
print(" x = ", x)

def only_words(x):
    res = x.split()
    for i in range(len(res)):
        res[i] = re.sub('[,:;.]', '', res[i])
    ser = ' '.join(res)
    return ser
print("only_words(x) = " , only_words(x) )

