# Segment Tree (Range Sum)
==========================
def build(arr):
    n = len(arr)
    tree = [0] * (2 * n)
    # insert leaves
