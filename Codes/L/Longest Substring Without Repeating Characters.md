# Longest Substring Without Repeating Characters
================================================
s = "abcabcbb"
char_set = set()

left = 0
max_len = 0

for right in range(len(s)):
    while s[right] in char_set:
        char_set.remove(s[left])
        left += 1
