import math
import sys
from bisect import bisect_left

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

left_elem = []
right_elem = []
for segment in segments:
    x = int(segment[0])
    y = int(segment[1])
    left_elem.append(x)
    right_elem.append(y)

left_elem.sort()
right_elem.sort()

print(left_elem)
print(right_elem)
print(points)

res = []
for point in points:
    left_side_lefter = bisect_left(left_elem, point)
    right_side_lefter = bisect_left(right_elem, point)
    res.append(left_side_lefter - right_side_lefter)

print(*res)





