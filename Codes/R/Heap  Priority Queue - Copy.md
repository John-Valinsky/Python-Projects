# Heap  Priority Queue
======================
import heapq

arr = [5, 1, 3, 7, 2]
heapq.heapify(arr)   # min-heap

heapq.heappush(arr, 0)
print(heapq.heappop(arr))  # smallest element
print(arr)