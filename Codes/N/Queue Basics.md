# Queue Basics
==============
from collections import deque

q = deque()
q.append(10)
q.append(20)
q.append(30)

print(q.popleft())  # 10
print(q)