import math

def checkPerfectNumber(num):
    arr = postivie_divisrors(num)
    if sum(arr) == num:
        return True
    else:
        return False


def postivie_divisrors(n):

        app = []
        for i in range(2,int(n**0.5)+1):
            if n%i ==0:
                app.append(i)
                if i != pow(n,0.5):
                    app.append(n//i)
        if n>1:
            app.append(1)
        return app

print(postivie_divisrors(2))
print(checkPerfectNumber(27))

