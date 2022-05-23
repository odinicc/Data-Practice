
# a number using Newtons method
def squareRoot(x,a,l):
    root = 0.5 * (x + (a / x))
    if(abs(root - x) >= l):
        root = squareRoot(root, a, l)
    return root

n = 427
l = 0.00001

root = squareRoot(n, n, l)
print("root",root)

# This code is contributed by AnkitRai01
