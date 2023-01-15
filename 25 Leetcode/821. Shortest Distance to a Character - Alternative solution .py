
def shortestToChar(S, C):
    ans = []
    ans.append(0 if S[0] == C else 10001)
    print(ans)
    for i in range(1,len(S)):
        if S[i] == C:
            ans.append(0)
        else:
            ans.append(ans[i-1] + 1)
    print(ans)
    for i in range(len(S)-2,-1,-1):
        ans[i] = min(ans[i], ans[i+1] + 1)

    print(ans)




s = "loveleetcode"
c = "e"
print(shortestToChar(s, c))


