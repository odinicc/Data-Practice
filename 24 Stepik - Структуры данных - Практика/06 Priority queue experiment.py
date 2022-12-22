
import queue


import sys
import math



q = queue.PriorityQueue()
q.put((-1, 10))
q.put((-1, 2))
q.put((-1, 4))
q.put((-1, 1))
q.get()
q.get()

q.put((-1, 6))
q.put((-1, 2))

print(q.queue)
print(q.get())




#%%
