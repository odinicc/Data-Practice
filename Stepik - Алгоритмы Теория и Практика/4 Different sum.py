def difsum(num):
    s = 0
    app = []
    if num ==1:
        return [1] , 1
    for i in range(1, num):
        if s < num < s + i :
            last = num - sum(app)
            app[i-2] += last
            return app, i-1
        elif s+i == num or num == 2:
            last = num - sum(app)
            app.append(last)
            return app, i
        s = s + i
        app.append(i)


num = int(input())
app , i= difsum(num)
print(i)
print(*app)
