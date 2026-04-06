# Graph Representation
======================
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0],
    3: [1],
    4: [1, 5],
    5: [4]
}

print(graph[1])  # neighbors of node 1