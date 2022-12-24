import math


#def isValid(self, s):
def isValid(s):
    stack = []
    if len(s) == 0:
        return True
    if len(s) == 1:
        return False
    for elem in s:
        if elem =='(' or elem =='{' or elem =='[':
            stack.append(elem)
        elif len(stack) == 0:
            return False
        elif elem ==')':
            if stack[-1] == '(':
                stack.pop()
            else:
                return False
        elif elem =='}':
            if stack[-1] == '{':
                stack.pop()
            else:
                return False
        elif elem ==']':
            if stack[-1] == '[':
                stack.pop()
            else:
                return False

    if len(stack) == 0:
        return True
    else:
        return False





print(isValid('()'))


