Sum & Max
=========
arr = [3, 7, 2, 9, 4]

total = 0
max_val = arr[0]

for num in arr:
    total += num
    if num > max_val:
        max_val = num
