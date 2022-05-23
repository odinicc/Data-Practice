import math
import sys

def read_data():

    #for local solution
    inf = open("10.txt")

    #for system solution
    #inf = sys.stdin

    lines = inf.readlines()
    first_line_input = lines[0].replace('\n', '')
    arr_1 = first_line_input.split(" ")
    arr_1.pop(0)
    arr_1 = list(map(int, arr_1))

    secondline_line_input = lines[1].replace('\n', '')
    arr_2 = secondline_line_input.split(" ")
    arr_2.pop(0)
    arr_2 = list(map(int, arr_2))


    return arr_1 , arr_2

def binary_search(arr,arr_start, arr_end, element):
    if arr_start < arr_end:
        arr_medium = math.floor((arr_start+arr_end)/2)
        #print("-- arr_medium", arr_medium , "|arr[arr_medium]", arr[arr_medium] ,"|arr_start", arr_start , "|arr_end", arr_end)
        if arr[arr_medium] == element:
            #print("ho")
            return arr_medium
        elif arr[arr_medium] < element:
            #print("arr_medium < element | arr_medium =", arr_medium, "|arr_start", arr_start, "|arr_end", arr_end)
            #print("hi")
            return binary_search(arr,arr_medium+1, arr_end, element)
        elif arr[arr_medium] > element:
            #print("arr_medium > element | arr_medium =", arr_medium, "|arr_start", arr_start, "arr_end", arr_end)
            #print("hi")
            return binary_search(arr, arr_start, arr_medium, element)
    else:
        return -1

arr_1 , arr_2 = read_data()


result = []

for i in arr_2:
    pos = binary_search(arr_1, 0, len(arr_1), i)
    if pos >= 0:
        result.append(pos+1)
    elif pos < 0:
        result.append(-1)


print(*result)

