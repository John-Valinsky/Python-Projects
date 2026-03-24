First Non-Repeating Character
=============================
s = "aabbccd"
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
