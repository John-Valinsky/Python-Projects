# Valid Parentheses
===================
s = "()[]{}"
stack = []

pairs = {')': '(', ']': '[', '}': '{'}
valid = True

for ch in s:
    if ch in pairs.values():
        stack.append(ch)
    else:
        if not stack or stack.pop() != pairs[ch]:
            valid = False

