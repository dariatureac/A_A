import time
import random
from collections import deque
import matplotlib.pyplot as plt


#  Graph generator

def generate_random_graph(n, p=0.05):
    """Random graph: each edge exists with probability p."""
    graph = {i: [] for i in range(n)}
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < p:
                graph[i].append(j)
                graph[j].append(i)
    return graph


#  BFS

def bfs(graph, start=0):
    visited = {start}
    queue = deque([start])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for nb in graph[node]:
            if nb not in visited:
                visited.add(nb)
                queue.append(nb)
    return order


#  DFS (iterative)

def dfs(graph, start=0):
    visited = set()
    stack = [start]
    order = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            order.append(node)
            for nb in reversed(graph[node]):
                if nb not in visited:
                    stack.append(nb)
    return order


#  Benchmarking

SIZES = [100, 500, 1000, 2500, 5000, 7500, 10000]
RUNS = 3


def run_suite(graph_fn, sizes):

    print(f"  {'n':>7}  |  {'BFS (s)':>12}  |  {'DFS (s)':>12}  |  {'DFS/BFS':>8}")

    bfs_times, dfs_times = [], []
    for n in sizes:
        g = graph_fn(n)
        bfs_runs = []
        dfs_runs = []
        for _ in range(RUNS):
            t0 = time.perf_counter()
            bfs(g, start=0)
            bfs_runs.append(time.perf_counter() - t0)

            t0 = time.perf_counter()
            dfs(g, start=0)
            dfs_runs.append(time.perf_counter() - t0)
        b = sum(bfs_runs) / RUNS
        d = sum(dfs_runs) / RUNS
        bfs_times.append(b)
        dfs_times.append(d)
        ratio = d / b if b > 0 else float('inf')
        print(f"  {n:>7}  |  {b:>12.6f}  |  {d:>12.6f}  |  {ratio:>8.3f}x")
    return bfs_times, dfs_times


if __name__ == "__main__":
    random.seed(42)

    print("       BFS vs DFS Empirical Comparison")
    print("       Random Graph (p = 0.05)")


    bfs_t, dfs_t = run_suite(generate_random_graph, SIZES)

    plt.figure(figsize=(9, 5))
    plt.plot(SIZES, bfs_t, marker='o', label='BFS', color='#2E75B6', linewidth=2)
    plt.plot(SIZES, dfs_t, marker='s', label='DFS', color='#E05A2B', linewidth=2)
    plt.title("BFS vs DFS — Random Graph (p = 0.05)", fontsize=14, fontweight='bold')
    plt.xlabel("Number of vertices (n)", fontsize=12)
    plt.ylabel("Execution time (seconds)", fontsize=12)
    plt.legend(fontsize=11)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()