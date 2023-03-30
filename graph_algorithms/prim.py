from queue import PriorityQueue as pq
def Prim(G,W):
    n=len(G)
    kolejka=pq()
    visited=[False for _ in range(n)]
    values=[float("inf") for _ in range(n)]
    parent=[None for _ in range(n)]
    kolejka.put((0,0))
    for i in range(n-1):
        kolejka.put((float("inf"),i))
    while not kolejka.empty():
        _,v=kolejka.get()
        if visited[v]:
            continue
        visited[v]=True
        for u in G[v]:
            if visited[u]:
                continue
            if W[v][u]<values[u]:
                parent[u]=v
                values[u]=W[v][u]
                kolejka.put(values[u],u)
    return parent