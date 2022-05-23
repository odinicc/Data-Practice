import math

for n in range(1,10):
    print(n,n*math.log(n,2))

print("----------------------")
for n in range(2,10):
    print(math.log(n,2)*math.log(3,2),math.log(3,n))


print("----------------------")

n=100000

print(round(math.log(math.log(n, 2)),2))
print(round(math.sqrt(math.log(n, 4)),2))

print(round(math.log(n, 3)))


print(round(math.log(n, 2) ** 2))
print(round(math.sqrt(n)))
print(round(n / math.log(n, 5)))
print(round(math.log(math.factorial(n),2)))
print(round(3 ** math.log(n, 2)))
print(round(n ** 2))
print(round(7 ** (math.log(n, 2))))
print(round(math.log(n, 2) ** (math.log(n, 2))))

print(round(n ** (math.log(n, 2))))

m = round(math.sqrt(n))
print(len(str(n ** m)))

print(len(str(2 ** n)))
print(len(str(4 ** n)))


print(len(str(round(2 ** (3 * n)))))

#print(round(math.factorial(n)))
#print(round(2 ** (2 ** n)))