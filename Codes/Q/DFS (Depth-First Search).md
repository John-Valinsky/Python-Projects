# DFS (Depth-First Search)
==========================
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    print(node, end=" ")

        for neighbor in graph[node]:
