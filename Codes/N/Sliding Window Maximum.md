# Sliding Window Maximum
========================
from collections import deque

arr = [1,3,-1,-3,5,3,6,7]
k = 3
dq = deque()
result = []

for i in range(len(arr)):
