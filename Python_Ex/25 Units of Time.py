from datetime import datetime
n = input("Enter n: ")
f = datetime.fromtimestamp(int(n)).strftime("%A, %B %d, %Y %I:%M:%S")
print('f = ',f)
