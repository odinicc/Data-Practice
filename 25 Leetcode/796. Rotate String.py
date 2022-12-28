import math

#def romanToInt(self, s):
def rotateString(s, goal):
    s = list(s)
    goal = list(goal)
    if len(s) == 0:
        if len(s) == 0:
            return True
        else:
            return False
    if len(s) != len(goal):
        return False

    if len(s) == 1:
        if s == goal:
            return True
        else:
            return False

    #take first element from first list (first_elem_s)
    first_elem_s = s[0]
    s_elem_in_goal = []
    #find elements similar to first_elem_s in second list
    for k in range(len(goal)):
        if goal[k]  == first_elem_s:
            s_elem_in_goal.append(k)
    # if in second list we can't find first_elem_s => Lists is not equal
    if len(s_elem_in_goal) ==0:
        return False
    print(s_elem_in_goal)
    for start in s_elem_in_goal:
        k = start
        d = 0
        while k != start - 1:
            if k < len(goal)-1:
                k += 1
            elif k == len(goal)-1 :
                k = 0
            d += 1
            print(goal[k], s[d])
            if goal[k] != s[d]:
                break
            if d == len(s)-1:
                return True
    return False


s = "bbbacddceeb"
goal = "ceebbbbacdd"
print(rotateString(s, goal))

