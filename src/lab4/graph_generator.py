import random

INF = float('inf')

def generate_sparse_graph(n, edge_prob=0.15):
    """Generate adjacency matrix for a sparse graph."""
    graph = [[INF] * n for _ in range(n)]
    for i in range(n):
        graph[i][i] = 0
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < edge_prob:
                w = random.randint(1, 100)
                graph[i][j] = w
                graph[j][i] = w
    return graph

def generate_dense_graph(n, edge_prob=0.80):
    """Generate adjacency matrix for a dense graph."""
    return generate_sparse_graph(n, edge_prob)