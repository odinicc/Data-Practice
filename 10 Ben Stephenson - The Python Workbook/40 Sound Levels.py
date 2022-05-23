import pprint
from tabulate import tabulate

x = {"Jackhammer" : 130, "Gas Lawnmower" : 106}
x["Alarm Clock"] = 70
x["Quiet Room"] = 40


for key, value in x.items():
    print(key, ' : ', value)

z = 80
closest_value =  min(x, key=lambda y:abs(float(x[y])-z)) 
print ('closest value to ', z, 'is',  closest_value, 'with', x[closest_value] )

