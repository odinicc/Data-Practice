import math

def fib(n):
    fib_arr = [0,1,1]
    if n > 2:
        for i in range(3,n+1):
            fib_arr.append(fib_arr[i-1]+fib_arr[i-2])
    print(fib_arr)
    return fib_arr[n]
nums = 10


print(fib(nums))

#%%
