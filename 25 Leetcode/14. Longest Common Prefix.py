import math

#def longestCommonPrefix(self, strs):
def longestCommonPrefix(strs):
    #convert to string
    strs = [str(x) for x in strs]
    l = len(strs)
    l_min = float('inf')
    max_len = ''
    #Find word with min lenght
    for word in strs:
        if len(word) <  l_min:
            l_min = len(word)
        if len(word) == 0:
            return ''

    for character in range(l_min):
        for word in range(len(strs)):
            temp_symb = strs[0][character]
            if strs[word][character] != temp_symb:
                break
        else:
            max_len = max_len + strs[0][character]
            continue

        break
    return max_len




strs = ["flower","flow","fr"]
print(longestCommonPrefix(strs))


