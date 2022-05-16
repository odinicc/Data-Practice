import heapq
import sys

def input_func():
    #for local solution
    inf = open('1.txt', 'r')

    #for system solution
    # inf = sys.stdin

    Lines = inf.readlines()
    Lines.pop(0)

    operations = []

    for Line in Lines:
        words = Line.split(" ")
        operation = words[0].replace('\n', '')
        try:
            number = int(words[1].replace('\n', ''))
            operations.append([operation, -number])
        except:
            operations.append([operation, None])

    return operations

def decoding(operations):
    li = []
    heapq.heapify(li)
    result = []
    for i in operations:
        op = i[0]
        val = i[1]
        if op == "Insert":
            heapq.heappush(li,val)
        elif op == "ExtractMax":
            result.append(-heapq.heappop(li))
    return result

def print_list(listt):
    for i in listt:
        print(i)

operations = input_func()
result = decoding(operations)
print_list(result)