# BFS (Breadth-First Search)
============================
from collections import deque

def bfs(graph, start):
    visited = set()
    q = deque([start])

    while q:
        node = q.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            q.extend([n for n in graph[node] if n not in visited])

bfs(graph, 0)