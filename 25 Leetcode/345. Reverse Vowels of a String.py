import math
import string

def count_vowels(s):
    vowels_list = ['a', 'e', 'i', 'o', 'u']
    i = 0
    vowels = []
    for letter in s:
        if letter in vowels_list:
            vowels.append(letter)
    return vowels

def reverseVowels(s):
    vowels = count_vowels(s)
    s = list(s)
    if len(vowels) < 2:
        return s
    else:

        for i in range(len(s)):
            if s[i] in ['a', 'e', 'i', 'o', 'u']:
                s[i] = vowels[-1]
                vowels.pop()
    result_string = ''.join(s)
    return result_string

s = "leetcode   "
print(reverseVowels(s))



