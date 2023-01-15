import math
import re

#def romanToInt(self, s):

def double_letters(arr):
    iter = 0
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            print('---',arr[i:j])
            if arr[i] == arr[j]:
                iter += 1
                break
    return iter

def buddyStrings(s, goal):
    if len(s) != len(goal):
        return False
    if len(s) < 2 or len(goal) < 2:
        return False
    not_eual = []
    s_na = []
    goal_na = []
    for i in range(len(s)):
        if s[i] != goal[i]:
            not_eual.append(i)
            s_na.append(s[i])
            goal_na.append(goal[i])
    s_na.sort()
    goal_na.sort()
    if s_na != goal_na:
        return False

    print('--',not_eual,double_letters(goal))
    if len(not_eual) == 2:
        return True
    else:
        if len(not_eual) == 0 and double_letters(goal) >= 1:
            return True
        else:
            return False



s = "abab"
goal = "abab"
#print(buddyStrings(s,goal))
print(double_letters(goal))
