
import queue


import sys
import math



q = queue.PriorityQueue()
q.put((-1, 10))
q.put((-1, 2))
q.put((-1, 4))
q.put((1, 1))
print(q.get())
q.get()
q.get()

q.put((-1, 6))
q.put((-1, 2))

print(q.queue)
m = q.get()
print(m)
print(m[1])
print(m[0])




