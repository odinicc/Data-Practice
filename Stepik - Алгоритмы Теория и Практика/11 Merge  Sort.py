import math
import sys
inv = 0

def read_data():

    #for local solution
    inf = open("11.txt")

    #for system solution
    #inf = sys.stdin

    lines = inf.readlines()

    secondline_line_input = lines[1].replace('\n', '')
    arr = secondline_line_input.split(" ")
    arr = list(map(int, arr))

    return arr

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    else:
        median = math.floor(len(arr) / 2)
        arr_1 = merge_sort(arr[:median])
        arr_2 = merge_sort(arr[median:])
        return merge_func(arr_1 , arr_2)

def merge_func(arr_1 , arr_2):
    global inv

    it_arr_1 = 0
    it_arr_2 = 0
    result = []
    while len(arr_1) - it_arr_1 != 0 or len(arr_2) - it_arr_2 != 0:
        if len(arr_1) - it_arr_1 > 0 and len(arr_2) - it_arr_2 > 0:
            if arr_1[it_arr_1] <= arr_2[it_arr_2]:
                result.append(arr_1[it_arr_1])
                print("arr_1 " , arr_1 , "it_arr_1 " , it_arr_1,"arr_2 " , arr_2 , "it_arr_2 " , it_arr_2 )
                it_arr_1 += 1

            elif arr_1[it_arr_1] > arr_2[it_arr_2]:
                result.append(arr_2[it_arr_2])

                it_arr_2 += 1


        elif len(arr_1) - it_arr_1 > 0 and len(arr_2) - it_arr_2 == 0:
            result.append(arr_1[it_arr_1])
            #inv += len(arr_1) - it_arr_1
            it_arr_1 += 1


        elif len(arr_1) - it_arr_1 == 0 and len(arr_2) - it_arr_2 > 0:
            result.append(arr_2[it_arr_2])
            #inv += len(arr_2) - it_arr_2
            it_arr_2 += 1

    return result


arr = read_data()

print("arr =",arr)

sort = merge_sort(arr)
print("inv =",inv)
print("sort = ",sort)


