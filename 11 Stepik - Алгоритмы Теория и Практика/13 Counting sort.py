import math
import sys

def read_data():
    #read from file
    inf = open("13.txt","r")

    #read from system input
    #inf = sys.stdin


    Lines  = inf.readlines()[1]
    List = list(Lines.split(" "))
    return List

def create_dic(Arr):
    Dict = {}
    for i in range(1, 11):
        Dict[i] = 0

    for elem in Arr:
        elem = int(elem)
        if 0 < elem and elem < 11:
            Dict[elem] += 1

    return Dict

def sort_arr(Arr,Dict):
    Overal_arr = []
    for i in range(1,11):
        for k in range(Dict[i]):
            Overal_arr.append(i)
    return Overal_arr

Arr = read_data()
Dict = create_dic(Arr)
Overal_arr = sort_arr(Arr,Dict)

print(*Overal_arr)


