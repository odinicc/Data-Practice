# Returns true if arr[i..n-1]
# represents a max-heap

def isHeap_MAX(arr, i, n):
    # If (2 * i) + 1 >= n, then leaf node, so return true
    if i >= int((n - 1) / 2):
        return True

    # If an internal node and is greater
    # than its children, and same is
    # recursively true for the children
    if (arr[i] >= arr[2 * i + 1] and
            arr[i] >= arr[2 * i + 2] and
            isHeap_MAX(arr, 2 * i + 1, n) and
            isHeap_MAX(arr, 2 * i + 2, n)):
        return True

    return False


def isHeap_MIN(arr, i, n):
    # If (2 * i) + 1 >= n, then leaf node, so return true
    if i >= int((n - 1) / 2):
        return True

    # If an internal node and is greater
    # than its children, and same is
    # recursively true for the children
    if (arr[i] <= arr[2 * i + 1] and
            arr[i] <= arr[2 * i + 2] and
            isHeap_MIN(arr, 2 * i + 1, n) and
            isHeap_MIN(arr, 2 * i + 2, n)):
        return True

    return False

def dec_isHeap(arr,type):
    if type == "MAX":
        n = len(arr) - 1
        if isHeap_MAX(arr, 0, n):
            return True
        else:
            return False
    elif type == "MIN":
        n = len(arr) - 1
        if isHeap_MIN(arr, 0, n):
            return True
        else:
            return False


arr1 = [2,4,5,12,5,6]
arr2 = [10,14,11]
arr3 = [3,20,6,30,21,30,5,31,60,30,31,31]
arr4 = [6,1,2]

print(dec_isHeap(arr1,"MIN"))
print(dec_isHeap(arr2,"MIN"))
print(dec_isHeap(arr3,"MIN"))
print(dec_isHeap(arr4,"MAX"))


