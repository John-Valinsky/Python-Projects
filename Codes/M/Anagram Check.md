# Anagram Check
===============
s = "listen"
t = "silent"

if len(s) != len(t):
    print(False)
else:
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

