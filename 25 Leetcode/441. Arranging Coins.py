import math


#def mergeTwoLists(self, list1, list2):
def arrangeCoins(n):
    row_val = 1
    while n >= row_val:
        n -= row_val
        row_val += 1
    return row_val-1



n = 3
print(arrangeCoins(n))
