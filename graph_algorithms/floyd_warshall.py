def floyd(G):
    n=len(G)
    for k in range(n):
        for u in range(n):
            for v in range(n):
                G[u][v]=min(G[u][v],G[u][k]+G[k][v])
    return G