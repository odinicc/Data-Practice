import math

#def romanToInt(self, s):
def romanToInt(x):
    l = list(x)
    le = len(l)
    if le == 0:
        return 0
    numb = 0
    cur_roman = 0
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(le-1,-1,-1):
        if roman_map[l[i]] >= cur_roman:
            numb += roman_map[l[i]]
            cur_roman = roman_map[l[i]]
        else:
            numb -= roman_map[l[i]]

        #print(l[i:] , numb)
    return numb



print(romanToInt('MCMXCIV'))

