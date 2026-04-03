# Detect Cycle
==============
slow = head
fast = head

has_cycle = False

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
