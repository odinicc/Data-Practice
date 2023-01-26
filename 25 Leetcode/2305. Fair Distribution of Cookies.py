import math

def distributeCookies(cookies, k):
    r = [0]*k
    cookies.sort(reverse=True)
    print(cookies)
    for ck in cookies:
        i_min = r.index(min(r))
        r[i_min] += ck
        print(r)
    return max(r)


cookies = [8,15,10,20,8]
k = 2
print(distributeCookies(cookies, k))


