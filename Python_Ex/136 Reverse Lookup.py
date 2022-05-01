d = {'one':1 , 'two':1  , 'three':3  }

def reverseLookup(d , n):
    l = []
    for i in d:
        if d[i] == n:
            l.append(i)
    return l

print(reverseLookup(d , 1))
    
