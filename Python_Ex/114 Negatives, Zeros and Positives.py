lis = [ 2, 3, -4, 1, 0, -1, 1, -2]
i=0
j = 0
while i < (len(lis)) and j < 10:
    if lis[i] > 0:
        t = lis.pop(i)
        lis.append(t)
        print(lis)
    else:
        i += 1
    j += 1

print(lis)
