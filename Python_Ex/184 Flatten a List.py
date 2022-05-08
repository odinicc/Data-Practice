data = [1, [2, 3], [4, [5, [6, 7]]], [[8, 9], 10]]

print("data",data)
print("data[0]",data[0])
print("type(data[0])",type(data[0]))
print("type(data[1])",type(data[1]))

if type(data[1]) == list:
    print(" Hey ")



def flatten(S):
    if S == []:
        return S
    if isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])

l2 = flatten(data)
print("data2 ",l2)