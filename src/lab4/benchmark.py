import time
import random
from graph_generator import generate_sparse_graph, generate_dense_graph
from dijkstra import dijkstra
from floyd_warshall import floyd_warshall

random.seed(42)

SIZES = [10, 50, 100, 200, 300, 500]
RUNS = 3  # average over this many runs

def benchmark_dijkstra(graph):
    t0 = time.perf_counter()
    for _ in range(RUNS):
        dijkstra(graph, 0)
    t1 = time.perf_counter()
    return (t1 - t0) / RUNS * 1000  # ms

def benchmark_floyd(graph):
    t0 = time.perf_counter()
    floyd_warshall(graph)
    t1 = time.perf_counter()
    return (t1 - t0) * 1000  # ms

def run_benchmark(graph_fn, label):

    print(f"  {label}")
    print(f"{'='*55}")
    print(f"{'n':>6} | {'Dijkstra (ms)':>15} | {'Floyd-Warshall (ms)':>20}")
    
    for n in SIZES:
        g = graph_fn(n)
        d_time = benchmark_dijkstra(g)
        fw_time = benchmark_floyd(g)
        print(f"{n:>6} | {d_time:>15.4f} | {fw_time:>20.4f}")

if __name__ == "__main__":
    run_benchmark(generate_sparse_graph, "SPARSE GRAPH (edge_prob=0.15)")
    run_benchmark(generate_dense_graph,  "DENSE GRAPH  (edge_prob=0.80)")