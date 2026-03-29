# Subarray Sum = K
==================
arr = [1, 2, 3]
k = 3

prefix_sum = 0
seen = {0: 1}
count = 0

for num in arr:
    prefix_sum += num
    if prefix_sum - k in seen:
        count += seen[prefix_sum - k]
    seen[prefix_sum] = seen.get(prefix_sum, 0) + 1
print(count)