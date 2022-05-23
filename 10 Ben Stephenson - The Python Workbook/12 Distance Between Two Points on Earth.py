import math as m

#batumi
t1 = 41.643414
g1 = 41.639900
#
t2 = 55.751244
g2 = 37.618423

distance = 6371.01*m.acos(m.sin(m.radians(t1))* m.sin(m.radians(t2)) + m.cos(m.radians(t1))*m.cos(m.radians(t2))*m.cos(m.radians(g1-g2)) )

print ('distance', distance)
