# Segment Tree (Range Sum)
==========================
def build(arr):
    n = len(arr)
    tree = [0] * (2 * n)
    # insert leaves
    for i in range(n):
        tree[n + i] = arr[i]
    # build tree
    for i in range(n - 1, 0, -1):
        tree[i] = tree[2 * i] + tree[2 * i + 1]
    return tree

arr = [1, 2, 3, 4]
tree = build(arr)
print(tree)