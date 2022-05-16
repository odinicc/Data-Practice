
import math
from io import StringIO

def show_tree(tree, total_width=60, fill=' '):
    """Pretty-print a tree.
    total_width depends on your input size"""
    output = StringIO()
    last_row = -1
    for i, n in enumerate(tree):
        if i:
            row = int(math.floor(math.log(i+1, 2)))
        else:
            row = 0
        if row != last_row:
            output.write('\n')
        columns = 2**row
        col_width = int(math.floor((total_width * 1.0) / columns))
        output.write(str(n).center(col_width, fill))
        last_row = row
    print (output.getvalue())
    print ('-' * total_width)
    return

#print of dictionary by rows
def print_dic(dic):
    for i in dic:
        print("%s:" % i, dic[i])

# create  dictionary from code
def create_dict(code):
    code_dic = {}
    code_sym = list(code)

    # create dict
    for sym in code_sym:
        if sym not in code_dic:
            code_dic[sym] = 1
        else:
            code_dic[sym] += 1

    return code_dic

# create tree from dict
def create_tree(dic):
    # sort dic by value
    dic2 = dict(sorted(dic.items(), key=lambda item: item[1]))
    # take lowest value and write it as a leaf
    tree = []
    first = next(iter(dic2))
    tree.append([first, 1])
    # delete lowest value from dict
    del dic2[first]
    # run loop through all values
    if len(dic2) > 0:
        for k, v in dic2.items():
            prev = tree[-1][0]
            n_val = str(prev) + str(k)
            tree.append([k, 0])
            tree.append([n_val, 1])
        tree.pop()
        tree.reverse()

    return tree

def create_code_from_tree(tree):
    code = {}
    for dic_elem in dic:
        temp_code = ""
        for tree_elem in tree:
            if dic_elem in tree_elem[0]:
                temp_code += str(tree_elem[1])
        code[dic_elem] = temp_code
    return code

def encryption(code ,code_dic ):
    code_l = list(code)
    result_string = ""
    for symbol in code_l:
        result_string += str(code_dic[symbol])
    return result_string


code = "a"
code = input()

dic = create_dict(code)
tree = create_tree(dic)
code_dic = create_code_from_tree(tree)
encryped_code = encryption(code ,code_dic )
print(len(code_dic), len(encryped_code))
print_dic(code_dic)
print(encryped_code)
