import random
import statistics

numb = []
for j in range(10):
    l = []
    print(j, end = ' ')
    for i in range(15):
        l.append(random.choices(("H","T"), k=1))
        print(l[i], end = ' ')
        if(i>1):
            if ( (l[i] == l[i-1]) and (l[i-1] == l[i-2])):
                #print("--", l[i-1], l[i-2], l[i-3], l[i-3], "--")
                numb.append(i+1)
                print("")
                break
    
print(numb)
print(statistics.mean(numb))
            


 
