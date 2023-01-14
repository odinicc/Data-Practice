import math

#def romanToInt(self, s):

def same_row(word):
    initial_row = 0
    first = "qwertyuiop"
    second = "asdfghjkl"
    third = "zxcvbnm"
    for i in range(len(word)):

        cur_sim = word[i].lower()

        if cur_sim in first:
            cur_sim_row = 1
        elif cur_sim in second:
            cur_sim_row = 2
        elif cur_sim in third:
            cur_sim_row = 3

        if initial_row == 0:
            initial_row = cur_sim_row
        else:
            if initial_row != cur_sim_row:
                return False
    return True


def findWords(words):
    return list(filter(same_row, words))





words = ["Hello","Alaska","Dad","Peace"]
word = "Peace"
print(findWords(words))
