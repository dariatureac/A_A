import random

def generate_graph(n, edge_prob=0.15):
    """
    Generate a random undirected weighted graph.
    Returns:
        edges: list of (weight, u, v) — for Kruskal
        adj:   adjacency list adj[u] = [(weight, v)] — for Prim
    """
    edges = []
    adj = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < edge_prob:
                w = random.randint(1, 100)
                edges.append((w, i, j))
                adj[i].append((w, j))
                adj[j].append((w, i))
    return edges, adj

def generate_sparse_graph(n):
    """Sparse graph: edge_prob = 0.15"""
    return generate_graph(n, edge_prob=0.15)

def generate_dense_graph(n):
    """Dense graph: edge_prob = 0.80"""
    return generate_graph(n, edge_prob=0.80)