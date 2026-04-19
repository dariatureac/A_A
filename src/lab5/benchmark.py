import time
import random
import matplotlib.pyplot as plt
from graph_generator import generate_sparse_graph, generate_dense_graph
from kruskal import kruskal
from prim import prim

random.seed(42)

SIZES = [10, 50, 100, 200, 300, 500, 750, 1000]
RUNS = 3

def bench(fn, *args):
    t0 = time.perf_counter()
    for _ in range(RUNS):
        fn(*args)
    return (time.perf_counter() - t0) / RUNS * 1000  # ms

def run_benchmark(graph_fn, label):
    kruskal_times = []
    prim_times = []
    print(f"\n{'='*52}")
    print(f"  {label}")
    print(f"{'='*52}")
    print(f"{'n':>6} | {'Kruskal (ms)':>14} | {'Prim (ms)':>12}")
    print(f"{'-'*6}-+-{'-'*14}-+-{'-'*12}")
    for n in SIZES:
        edges, adj = graph_fn(n)
        k_time = bench(kruskal, n, edges)
        p_time = bench(prim, n, adj)
        kruskal_times.append(k_time)
        prim_times.append(p_time)
        print(f"{n:>6} | {k_time:>14.4f} | {p_time:>12.4f}")
    return kruskal_times, prim_times

if __name__ == "__main__":
    sparse_k, sparse_p = run_benchmark(generate_sparse_graph, "SPARSE GRAPH (edge_prob = 0.15)")
    dense_k,  dense_p  = run_benchmark(generate_dense_graph,  "DENSE GRAPH  (edge_prob = 0.80)")

    # --- plot results ---
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    axes[0].plot(SIZES, sparse_k, 'o-', color='#2196F3', lw=2, ms=6, label='Kruskal')
    axes[0].plot(SIZES, sparse_p, 's-', color='#F44336', lw=2, ms=6, label='Prim')
    axes[0].set_title('Sparse Graph (edge_prob=0.15)', fontweight='bold')
    axes[0].set_xlabel('Number of Nodes (n)')
    axes[0].set_ylabel('Execution Time (ms)')
    axes[0].legend(); axes[0].grid(True, alpha=0.3)

    axes[1].plot(SIZES, dense_k, 'o-', color='#4CAF50', lw=2, ms=6, label='Kruskal')
    axes[1].plot(SIZES, dense_p, 's-', color='#FF9800', lw=2, ms=6, label='Prim')
    axes[1].set_title('Dense Graph (edge_prob=0.80)', fontweight='bold')
    axes[1].set_xlabel('Number of Nodes (n)')
    axes[1].set_ylabel('Execution Time (ms)')
    axes[1].legend(); axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('lab7_results_chart.png', dpi=150, bbox_inches='tight')
    print("\nSaved: lab7_results_chart.png")
    plt.show()