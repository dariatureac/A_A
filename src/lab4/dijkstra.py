import heapq

INF = float('inf')

def dijkstra(graph, src):

    n = len(graph)
    dist = [INF] * n
    dist[src] = 0
    visited = [False] * n
    pq = [(0, src)]  # (distance, node)

    while pq:
        d, u = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True
        for v in range(n):
            if graph[u][v] < INF and not visited[v]:
                new_dist = d + graph[u][v]
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(pq, (new_dist, v))
    return dist