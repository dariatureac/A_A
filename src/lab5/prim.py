import heapq

def prim(n, adj):

    visited = [False] * n
    visited[0] = True
    heap = list(adj[0])   # start from vertex 0
    heapq.heapify(heap)
    mst_weight = 0

    while heap:
        w, v = heapq.heappop(heap)
        if visited[v]:
            continue
        visited[v] = True
        mst_weight += w
        for edge in adj[v]:
            if not visited[edge[1]]:
                heapq.heappush(heap, edge)

    return mst_weight