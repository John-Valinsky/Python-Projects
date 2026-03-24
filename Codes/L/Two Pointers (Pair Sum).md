Two Pointers (Pair Sum)
=======================
arr = [1, 2, 3, 4, 6]
target = 6

left = 0
right = len(arr) - 1

found = False

while left < right:
    current_sum = arr[left] + arr[right]

    if current_sum == target:
        found = True
        print(arr[left], arr[right])
