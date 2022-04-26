import random
import string


pas_let = ''.join(random.choices(string.ascii_uppercase, k=3))
pas_dig = ''.join(random.choices(string.digits, k=4))
pas =   pas_let + pas_dig
print(pas)


x ="234R2dfdf34"

def goodpass(x):
    if len(x)<8:
        return False
    elif x.islower() == True:
        return False
    elif x.isupper() == True:
        return False
    else:
        return True

def gen(N):
    pas_let = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=N))
    return pas_let

def generategoopass(N):
    a = 1
    while a == 1:
        pas = gen(N)
        if goodpass(pas) == True:
            return pas
            break
    

print(generategoopass(9))
