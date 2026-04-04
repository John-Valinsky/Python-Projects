# Level Order (BFS)
===================
from collections import deque

def level_order(root):
    if not root:
        return
    q = deque([root])
