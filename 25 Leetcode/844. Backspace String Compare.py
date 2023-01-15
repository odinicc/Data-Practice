import math
import string

# find and return all positions of "lse" element
# in "element" list
def indices(lst, element):
    result = []
    offset = -1
    while True:
        try:
            offset = lst.index(element, offset+1)
        except ValueError:
            return result
        result.append(offset)

def findClosest(arr, n, target):

    # Corner cases
    if (target <= arr[0]):
        return arr[0]
    if (target >= arr[n - 1]):
        return arr[n - 1]

    # Doing binary search
    i = 0; j = n; mid = 0
    while (i < j):
        mid = (i + j) // 2

        if (arr[mid] == target):
            return arr[mid]

        # If target is less than array
        # element, then search in left
        if (target < arr[mid]) :

            # If target is greater than previous
            # to mid, return closest of two
            if (mid > 0 and target > arr[mid - 1]):
                return getClosest(arr[mid - 1], arr[mid], target)

            # Repeat for left half
            j = mid

        # If target is greater than mid
        else :
            if (mid < n - 1 and target < arr[mid + 1]):
                return getClosest(arr[mid], arr[mid + 1], target)

            # update i
            i = mid + 1

    # Only single element left after search
    return arr[mid]


# Method to compare which one is the more close.
# We find the closest by taking the difference
# between the target and both values. It assumes
# that val2 is greater than val1 and target lies
# between these two.
def getClosest(val1, val2, target):

    if (target - val1 >= val2 - target):
        return val2
    else:
        return val1




def shortestToChar(s, c):
    m = float('inf')
    arr = [m]*len(s)

    for i in range(len(s)):
        if s[i] == c:
            arr[i] = 0

    null_pos = indices(arr,0)

    for i in range(len(arr)):
        if arr[i] == 0:
            continue
        else:
            closeset = findClosest(null_pos, len(null_pos), i)
            arr[i] = abs(closeset-i)

    return arr





s = "ed"
c = "e"
print(shortestToChar(s, c))


