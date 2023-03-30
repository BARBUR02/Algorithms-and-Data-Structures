from queue import PriorityQueue as pq
def Djikstra(G,W):
    n=len(G)
    parent=[None for _ in range(n)]
    d=[float("inf") for _ in range(n)]
    visited=[False for _ in range(n)]
    kolejka=pq()
    kolejka.put((0,0))
    for i in range(1,n):
        kolejka.put((float("inf"),i))
    while not kolejka.empty():
        _,v=kolejka.get()
        if visited[v]:
            continue
        visited[v]=True
        for u in G[v]:
            if W[v][u]+d[v]<d[u]:
                d[u]=W[v][u]+d[v]
                parent[u]=v
                kolejka.put((d[u],u))
    return parent