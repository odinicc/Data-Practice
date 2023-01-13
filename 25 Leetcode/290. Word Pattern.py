import math
import string


def check_value_exist(test_dict, value):
    do_exist = False
    for key, val in test_dict.items():
        if val == value:
            do_exist = True
    return do_exist

def wordPattern(pattern, s):
    s = s.split(' ')
    if len(s) != len(pattern):
        return False
    else:
        print(map(pattern.find, s))



pattern = "abba"
s = "dog cat cat fish"
print(wordPattern(pattern ,s))


