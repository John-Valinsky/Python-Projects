# Reverse a Linked List
=======================
prev = None
current = head

while current:
    nxt = current.next
    current.next = prev
