import math


#def plusOne(self, digits):
def searchInsert(nums, target):
    start = 0
    finish = len(nums)-1
    while start < finish:

        mid = (start + finish)//2
        print(start, ' ',mid, ' ',finish)
        print(nums[start], ' ',nums[mid], ' ',nums[finish])
        if mid == start or mid == finish:
            if nums[start] < target:
                mid += 1
            if nums[finish] < target:
                mid += 1
            break

        if nums[mid] < target:
            start = mid
        elif nums[mid] > target:
            finish = mid
        else:
            break
        print('    ')

    print('mid ',mid)
    return mid


nums = [1,3,5,6]
target = 7
print(searchInsert(nums, target))

