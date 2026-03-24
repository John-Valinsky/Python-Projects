Reverse String (Two-Pointer)
============================
s = list("hello")
left = 0
right = len(s) - 1

while left < right:
    s[left], s[right] = s[right], s[left]


