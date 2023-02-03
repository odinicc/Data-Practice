import math



def duplicateZeros(arr):
    i=0
    l = len(arr)
    while i < l:
        if arr[i] ==0:
            arr.insert(i,0)
            i += 1
        i += 1
    return arr[0:l]

arr = [1,0,2,3,0,4,5,0]
print(duplicateZeros(arr))

