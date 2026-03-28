# Count Frequencies
===================
arr = [1, 2, 2, 3, 3, 3]
freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1
