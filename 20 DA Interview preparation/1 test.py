l = [11,12,13,14,15,16] 
print(l)
le = len(l)
for i in l:
    print(l[le-l.index(i)-1])

