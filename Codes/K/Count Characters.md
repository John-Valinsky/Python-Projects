Count Characters
================
s = "interview"
freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
