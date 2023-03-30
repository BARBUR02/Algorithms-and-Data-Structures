def relax(u,v,W,parent,d):
    if W[u][v]+d[u]<d[v]:
        parent[v]=u
        d[v]=W[u][v]+d[u]


def belman_ford(G,W):
    n=len(G) # jakos wyliczona
    d=[float("inf") for _ in range(n)]
    parent=[None for _ in range(n)]
    d[0]=0 # wierzcholek startowy
    for i in range(n-1):
        for u,v in G:
            relax(u,v,W,parent,d)
    for u,v in G:
        if d[v]>d[u]+W[u][v]:
            print("cykl ujemny!")
            return
    return parent