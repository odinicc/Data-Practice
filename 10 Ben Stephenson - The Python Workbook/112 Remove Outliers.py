import heapq

lis =[12, 23, 10, 23, 1, 40, 2, 5]
print(lis)

def out(lis,n):
    sm = (heapq.nsmallest(n,lis))
    ls  = (heapq.nlargest(n,lis))
    gis = lis
    for i in range(len(sm)):
        gis.remove(sm[i])
    for j in range(len(ls)):
        gis.remove(ls[j])
    return gis
    
x = out(lis,2)
print(x)
