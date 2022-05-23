a = 3

for k in range(2,50,2):
    
    if k%4 == 2:
        d = 1
    else:
        d = -1
    a = a + d*4/(k * (k+1) * (k+2))
    print(k , " - ", k+1 ," - ", k+2, " - ",  a," - ", d) 
