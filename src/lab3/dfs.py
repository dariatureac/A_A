import time
import random
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


#  DFS algorithm

def dfs(graph, start=0):

    visited = set()
    stack = [start]
    order = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            order.append(node)
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

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
            dfs(g, start=0)
            runs.append(time.perf_counter() - t0)
        avg = sum(runs) / RUNS
        times.append(avg)
        print(f"  {n:>7}  |  {avg:>12.6f}")

    return times


if __name__ == "__main__":
    random.seed(42)

    print("       DFS Empirical Analysis")
    print("       Random Graph (p = 0.05)")


    random_t = measure(generate_random_graph, SIZES)

    plt.figure(figsize=(9, 5))
    plt.plot(SIZES, random_t, marker='o', label='Random (p = 0.05)', color='#E05A2B', linewidth=2)
    plt.title("DFS — Execution Time (Random Graph)", fontsize=14, fontweight='bold')
    plt.xlabel("Number of vertices (n)", fontsize=12)
    plt.ylabel("Execution time (seconds)", fontsize=12)
    plt.legend(fontsize=11)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()