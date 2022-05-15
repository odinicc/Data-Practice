import math
import sys

def read_data():
    #read from file
    inf = open("12.txt","r")

    #read from system input
    #inf = sys.stdin

    segments = []

    Lines  = inf.readlines()
    for line in Lines:
        words = line.split(" ")
        x = words[0]
        y = words[1].replace('\n', '')
        z = [x,y]
        segments.append(z)
    segments.pop()
    segments.pop(0)

    last_line = (Lines[-1])
    points = last_line.split(" ")
    points = [int(i) for i in points]
    return segments, points


def bin_search_pos(arr, element, type):
    pos = binary_search(arr, 0, len(arr), element)
    if pos == -1:
        return 0

    if type == "first":
        p = pos
        while arr[p] == arr[pos]:
            p -= 1
            return p
    elif type == "last":
        p = pos
        while arr[p] == arr[pos]:
            p += 1
            return p

'''
def bin_search_pos(arr, element, type):
    pos = binary_search(arr, 0, len(arr), element)

    if pos < 0:
        return 0

    if type == "first":
        if pos > 0:
            while pos>0 and arr[pos-1] == element:
                pos -= 1
                return pos
        elif pos == 1:
            return pos

    if type == "last":
        l = len(arr)
        if pos < l-1:
            for p in range(pos,l-1):
                if arr[p] != element or p == l-1:
                    return p
        elif pos == l-1:
            return pos+1

'''

def binary_search(arr,arr_start, arr_end, element):
    if arr_start < arr_end:
        arr_medium = math.floor((arr_start+arr_end)/2)
        #print("-- arr_medium", arr_medium , "|arr[arr_medium]", arr[arr_medium] ,"|arr_start", arr_start , "|arr_end", arr_end)
        if arr[arr_medium] == element:
            #print("ho")
            return arr_medium
        elif arr[arr_medium] <= element:
            #print("arr_medium < element | arr_medium =", arr_medium, "|arr_start", arr_start, "|arr_end", arr_end)
            #print("hi")
            return binary_search(arr,arr_medium+1, arr_end, element)
        elif arr[arr_medium] > element:
            #print("arr_medium > element | arr_medium =", arr_medium, "|arr_start", arr_start, "arr_end", arr_end)
            #print("hi")
            return binary_search(arr, arr_start, arr_medium, element)
    else:
        return -1


segments, points = read_data()

first_elem = []
last_elem = []
for segment in segments:
    x = int(segment[0])
    y = int(segment[1])
    first_elem.append(x)
    last_elem.append(y)

first_elem.sort()
last_elem.sort()

print(first_elem)
print(last_elem)

pos = bin_search_pos(last_elem, 3, "first")
print("pos = ",pos)

cross = []
'''
for point in points:
    N1 = bin_search_pos(first_elem, point, "last")
    N2 = bin_search_pos(last_elem, point, "first")
    print("point =", point, "N1 = ",N1,"|N2 = ",N2,"|type(N1) = ",type(N1),"|type(N2) = ",type(N2))
    N = N1 - N2
    cross.append(N)
'''
print(*cross)


