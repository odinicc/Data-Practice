import math
import sys

def read_data():

    #for local solution
    inf = open("11.txt")

    #for system solution
    #inf = sys.stdin

    lines = inf.readlines()

    secondline_line_input = lines[1].replace('\n', '')
    arr_2 = secondline_line_input.split(" ")
    arr_2.pop(0)
    arr_2 = list(map(int, arr_2))

    return arr_2
''' 
def merge_sort(arr):
    if len(arr) == 1:
        return arr
    elif len(arr) == 2:
        if arr[0]<arr[1]:
            return arr
        else:
            return [arr[1],arr[0]]
    else:
        median = math.floor(len(arr) / 2)
        arr_1 = merge_sort(arr[:median])
        arr_2 = merge_sort(arr[median:])
        return merge_func(arr_1 , arr_2)
'''
def merge_sort(arr):
    if len(arr) == 1:
        return arr
    else:
        median = math.floor(len(arr) / 2)
        arr_1 = merge_sort(arr[:median])
        arr_2 = merge_sort(arr[median:])
        return merge_func(arr_1 , arr_2)


def merge_func(arr_1 , arr_2):
    it_arr_1 = 0
    it_arr_2 = 0
    result = []
    while len(arr_1) - it_arr_1 != 0 or len(arr_2) - it_arr_2 != 0:
        if len(arr_1) - it_arr_1 > 0 and len(arr_2) - it_arr_2 > 0:
            if arr_1[it_arr_1] <= arr_2[it_arr_2]:
                result.append(arr_1[it_arr_1])
                it_arr_1 += 1
            elif arr_1[it_arr_1] > arr_2[it_arr_2]:
                result.append(arr_2[it_arr_2])
                it_arr_2 += 1

        elif len(arr_1) - it_arr_1 > 0 and len(arr_2) - it_arr_2 == 0:
            result.append(arr_1[it_arr_1])
            it_arr_1 += 1


        elif len(arr_1) - it_arr_1 == 0 and len(arr_2) - it_arr_2 > 0:
            result.append(arr_2[it_arr_2])
            it_arr_2 += 1

    return result



arr = read_data()
arr = [2,6,5,7,2,12,15,20,1,88,8]


arr_1 = [2,6,7,12,15,20]
arr_2 = [3,4,8,9,10,12]
print("arr1",arr_1)
print("arr2",arr_2)
result  = merge_func(arr_1 , arr_2)
print("result",result)

print("arr =",arr)
sort = merge_sort(arr)
print("sort = ",sort)


