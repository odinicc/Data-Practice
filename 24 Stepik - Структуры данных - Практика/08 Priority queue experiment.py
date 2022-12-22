
import queue


import sys
import math



q = queue.PriorityQueue()
q.put((2, -1))
q.put((1, -2))
q.put((4, -3))

print(q.queue)
print(q.get())



