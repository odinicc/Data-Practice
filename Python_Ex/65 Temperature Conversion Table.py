import pandas as pd
import pprint

my_new_dict = {}
for x in range(-50, 50):
    my_new_dict[x] = round((x*9)/5 + 32, 2)

pp = pprint.PrettyPrinter(indent=4,width=80)
pp.pprint(my_new_dict)

#print("C"," - ","F")
#for x in my_new_dict:
#    print(x," - ",my_new_dict[x])
