




def bubble_sort(nums):
    if len(nums) == 1:
        return nums
    else:
        if nums[1]< nums[0]:
            nums[0], nums[1]= nums[1], nums[0]
        # 0 and 1 index sorted
        for sort_item in range(2,len(nums)):
            elem = nums[sort_item]
            for bull in range(sort_item-1,-1,-1):
                print(bull,sort_item)
                if nums[bull+1] < nums[bull]:
                    nums[bull] , nums[bull+1] = nums[bull+1] , nums[bull]
                print(nums)
            print('----')

    print(nums)



nums = [10,5,80,90,23,2,20]
print(bubble_sort(nums))




