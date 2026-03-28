# Two Sum
=========
arr = [2, 7, 11, 15]
target = 9

seen = {}

for i, num in enumerate(arr):
    needed = target - num
    if needed in seen:
        print(seen[needed], i)
