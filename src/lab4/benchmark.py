import time
import random
import matplotlib.pyplot as plt
from graph_generator import generate_sparse_graph, generate_dense_graph
from dijkstra import dijkstra
from floyd_warshall import floyd_warshall

random.seed(42)

SIZES = [10, 50, 100, 200, 300, 500]
RUNS = 3

def bench_dijkstra(graph):
    t0 = time.perf_counter()
    for _ in range(RUNS):
        dijkstra(graph, 0)
    return (time.perf_counter() - t0) / RUNS * 1000  # ms

def bench_floyd(graph):
    t0 = time.perf_counter()
    floyd_warshall(graph)
    return (time.perf_counter() - t0) * 1000  # ms

def run_benchmark(graph_fn, label):
    dijkstra_times = []
    floyd_times = []
    print(f"\n{'='*55}")
    print(f"  {label}")
    print(f"{'='*55}")
    print(f"{'n':>6} | {'Dijkstra (ms)':>15} | {'Floyd-Warshall (ms)':>20}")
    print(f"{'-'*6}-+-{'-'*15}-+-{'-'*20}")
    for n in SIZES:
        g = graph_fn(n)
        d_time = bench_dijkstra(g)
        fw_time = bench_floyd(g)
        dijkstra_times.append(d_time)
        floyd_times.append(fw_time)
        print(f"{n:>6} | {d_time:>15.4f} | {fw_time:>20.4f}")
    return dijkstra_times, floyd_times

if __name__ == "__main__":
    sparse_d, sparse_fw = run_benchmark(generate_sparse_graph, "SPARSE GRAPH (edge_prob = 0.15)")
    dense_d,  dense_fw  = run_benchmark(generate_dense_graph,  "DENSE GRAPH  (edge_prob = 0.80)")

    # --- plot results ---
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    axes[0].plot(SIZES, sparse_d,  'o-', color='#2196F3', lw=2, ms=6, label='Dijkstra')
    axes[0].plot(SIZES, sparse_fw, 's-', color='#F44336', lw=2, ms=6, label='Floyd-Warshall')
    axes[0].set_title('Sparse Graph (edge_prob=0.15)', fontweight='bold')
    axes[0].set_xlabel('Number of Nodes (n)')
    axes[0].set_ylabel('Execution Time (ms)')
    axes[0].set_yscale('log')
    axes[0].legend(); axes[0].grid(True, alpha=0.3)

    axes[1].plot(SIZES, dense_d,  'o-', color='#4CAF50', lw=2, ms=6, label='Dijkstra')
    axes[1].plot(SIZES, dense_fw, 's-', color='#FF9800', lw=2, ms=6, label='Floyd-Warshall')
    axes[1].set_title('Dense Graph (edge_prob=0.80)', fontweight='bold')
    axes[1].set_xlabel('Number of Nodes (n)')
    axes[1].set_ylabel('Execution Time (ms)')
    axes[1].set_yscale('log')
    axes[1].legend(); axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('results_chart.png', dpi=150, bbox_inches='tight')
    print("\nSaved: results_chart.png")
    plt.show()