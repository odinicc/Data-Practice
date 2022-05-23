import statistics 

def med(a,b,c):
    x = statistics.median({a,b,c})
    return x

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
print("Median = ", med(a,b,c))


 
