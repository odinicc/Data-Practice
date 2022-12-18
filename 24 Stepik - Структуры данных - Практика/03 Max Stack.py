
# Если скобки в s расставлены правильно, выведите
# строку “Success". В противном случае выведите индекс (исполь-
# зуя индексацию с единицы) первой закрывающей скобки, для
# которой нет соответствующей открывающей. Если такой нет,
# выведите индекс первой открывающей скобки, для которой нет
# соответствующей закрывающей.

import sys

def read_data():
    # for local solution
    inf = '[]([];'

    # for system solution
    # inf = sys.stdin.read()

    return inf


def check_brackets(s):
    list_s = list(s)
    # stack for symbols like ( )
    classic_brackets = []
    straight_brackets = []
    curly_brackets = []
    # if we found closed bracket without open we assign its position to pfcb
    pfcb = -1

    for char_iter in range(len(list_s)):
        # regular brackets
        if list_s[char_iter] == '(':
            #classic_brackets.append(char_iter)
            classic_brackets.insert(0,char_iter)
        elif list_s[char_iter] == ')':
            if len(classic_brackets) > 0:
                classic_brackets.pop()
            else:
                pfcb = char_iter
                return pfcb+1
                break
        #straight brackets
        elif list_s[char_iter] == '[':
            #straight_brackets.append(char_iter)
            straight_brackets.insert(0,char_iter)
        elif list_s[char_iter] == ']':
            if len(straight_brackets) > 0:
                straight_brackets.pop()
            else:
                pfcb = char_iter
                return pfcb+1
                break
        #curly brackets
        elif list_s[char_iter] == '{':
            #curly_brackets.append(char_iter)
            curly_brackets.insert(0,char_iter)
        elif list_s[char_iter] == '}':
            if len(curly_brackets) > 0:
                curly_brackets.pop()
            else:
                pfcb = char_iter
                return pfcb+1
                break

    all_brackets = curly_brackets+ straight_brackets + classic_brackets
    if len(all_brackets) == 0:
        return 'Success'
    else:
        return min(all_brackets)+1


s = read_data()
print(check_brackets(s))




