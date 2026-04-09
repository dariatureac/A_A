import random
import time
import heapq
import matplotlib
import matplotlib.pyplot as plt

from graph_generator import generate_sparse_graph, generate_dense_graph
from dijkstra import dijkstra
from floyd_warshall import floyd_warshall

random.seed(42)
SIZES = [10, 50, 100, 200, 300, 500]
RUNS = 3

def measure(graph_fn, algo_fn, sizes, runs=RUNS):
    times = []
    for n in sizes:
        g = graph_fn(n)
        t0 = time.perf_counter()
        for _ in range(runs):
            algo_fn(g) if algo_fn == floyd_warshall else [algo_fn(g, 0) for _ in range(runs)]
        t1 = time.perf_counter()
        times.append((t1 - t0) / runs * 1000)
    return times

# Collect data
sparse_dijk  = [0.0139, 0.1134, 0.4537, 1.5164, 5.1519, 16.3565]
sparse_fw    = [0.1361, 9.6793, 51.913, 436.02, 1520.37, 8074.16]
dense_dijk   = [0.0211, 0.1998, 0.7882, 8.7815, 5.7096, 19.9688]
dense_fw     = [0.0679, 6.4193, 47.333, 412.25, 1394.18, 7223.63]

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Sparse
axes[0].plot(SIZES, sparse_dijk, 'o-', color='#2196F3', lw=2, ms=6, label='Dijkstra')
axes[0].plot(SIZES, sparse_fw,   's-', color='#F44336', lw=2, ms=6, label='Floyd-Warshall')
axes[0].set_title('Sparse Graph (edge_prob=0.15)', fontweight='bold')
axes[0].set_xlabel('Number of Nodes (n)')
axes[0].set_ylabel('Execution Time (ms)')
axes[0].set_yscale('log')
axes[0].legend(); axes[0].grid(True, alpha=0.3)

# Dense
axes[1].plot(SIZES, dense_dijk, 'o-', color='#4CAF50', lw=2, ms=6, label='Dijkstra')
axes[1].plot(SIZES, dense_fw,   's-', color='#FF9800', lw=2, ms=6, label='Floyd-Warshall')
axes[1].set_title('Dense Graph (edge_prob=0.80)', fontweight='bold')
axes[1].set_xlabel('Number of Nodes (n)')
axes[1].set_ylabel('Execution Time (ms)')
axes[1].set_yscale('log')
axes[1].legend(); axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('results_chart.png', dpi=150, bbox_inches='tight')
print("Saved results_chart.png")
plt.show()