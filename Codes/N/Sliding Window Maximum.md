# Sliding Window Maximum
========================
from collections import deque

arr = [1,3,-1,-3,5,3,6,7]
k = 3
dq = deque()
result = []

for i in range(len(arr)):
    while dq and dq[0] <= i - k:
        dq.popleft()

    while dq and arr[dq[-1]] < arr[i]:
        dq.pop()

    dq.append(i)

    if i >= k - 1:
        result.append(arr[dq[0]])
