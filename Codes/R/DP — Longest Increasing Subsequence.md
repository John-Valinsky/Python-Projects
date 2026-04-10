# DP — Longest Increasing Subsequence
=====================================
def lis(arr):
    n = len(arr)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
