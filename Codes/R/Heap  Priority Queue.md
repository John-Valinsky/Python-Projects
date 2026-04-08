# Dijkstra’s Shortest Path (Weighted Graph)
===========================================
import heapq

graph = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: []
}

def dijkstra(graph, start):
    heap = [(0, start)]
    dist = {node: float('inf') for node in graph}
    dist[start] = 0

    while heap:
        d, node = heapq.heappop(heap)
        if d > dist[node]:
            continue
        for neighbor, weight in graph[node]:
            if dist[node] + weight < dist[neighbor]:
                dist[neighbor] = dist[node] + weight
                heapq.heappush(heap, (dist[neighbor], neighbor))
    
    return dist

print(dijkstra(graph, 0))