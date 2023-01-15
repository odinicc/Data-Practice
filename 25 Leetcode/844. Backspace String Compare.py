

def backspaceCompare(s, t):
    s_stack = []
    t_stack = []
    for i in range(len(s)):
        if len(s_stack) > 0 and s[i] == '#':
            s_stack.pop()
        elif s[i] != '#':
            s_stack.append(s[i])

    for i in range(len(t)):
        if len(t_stack) > 0 and t[i] == '#':
            t_stack.pop()
        elif t[i] != '#':
            t_stack.append(t[i])

    if s_stack == t_stack:
        return True
    else:
        return False





s = "ab#c"
t = "ad#c"
print(backspaceCompare(s, t))


