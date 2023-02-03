import itertools

#print(itertools.groupby('haalllooo'))

k = itertools.groupby('haalllooo')
for key in k:
    print(key[0])

