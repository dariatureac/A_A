import time
import random
from collections import deque
import matplotlib.pyplot as plt

#  Graph generator

def generate_random_graph(n, p=0.3):
    """Random graph: each edge exists with probability p."""
    graph = {i: [] for i in range(n)}
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < p:
                graph[i].append(j)
                graph[j].append(i)
    return graph


#  BFS algorithm

def bfs(graph, start=0):
    """
    Breadth-First Search (iterative, using deque).
    Visits all nodes reachable from `start` in level-order.

    Time complexity:  O(V + E)
    Space complexity: O(V)

    Returns the list of visited nodes in BFS order.
    """
    visited = {start}
    queue = deque([start])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


#  Benchmarking

SIZES = [100, 500, 1000, 2500, 5000, 7500, 10000]
RUNS = 3


def measure(graph_fn, sizes):
    print(f"  {'n':>7}  |  {'Time (s)':>12}")
    times = []
    for n in sizes:
        runs = []
        for _ in range(RUNS):
            g = graph_fn(n)
            t0 = time.perf_counter()
            bfs(g, start=0)
            runs.append(time.perf_counter() - t0)
        avg = sum(runs) / RUNS
        times.append(avg)
        print(f"  {n:>7}  |  {avg:>12.6f}")
    return times


if __name__ == "__main__":
    random.seed(42)

    print("       BFS Empirical Analysis")
    print("       Random Graph (p = 0.05)")

    random_t = measure(generate_random_graph, SIZES)

    plt.figure(figsize=(9, 5))
    plt.plot(SIZES, random_t, marker='o', label='Random (p = 0.05)', color='#2E75B6', linewidth=2)
    plt.title("BFS — Execution Time (Random Graph)", fontsize=14, fontweight='bold')
    plt.xlabel("Number of vertices (n)", fontsize=12)
    plt.ylabel("Execution time (seconds)", fontsize=12)
    plt.legend(fontsize=11)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()