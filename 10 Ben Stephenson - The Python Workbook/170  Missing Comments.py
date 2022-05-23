import pprint

pp = pprint.PrettyPrinter(indent=4)

file_name = "Time11.py"

inf = open(file_name,'r')
Lines = inf.readlines()
arr= []

for line in Lines:
    line = line.replace('\n', '')
    arr.append(line)

pp.pprint(arr)

for i in range(len(arr)):
    row = arr[i]
    if len(row)>0:
        if row.startswith("def"):
            print("====")
            print("row - 1 = ", arr[i - 1])
            print("row = ",row)
            print("====")
            if not(arr[i-1].startswith("#")):
                print(arr[i-1])
                print(row)
                print('------')


