from collections import deque

def BFS(G):
    n=len(G)
    visited=[False for _ in range(n)]
    path_len=[0 for _ in range(n)]
    parent=[None for _ in range(n)]
    kolejka=deque()
    kolejka.append(0)
    visited[0]=True
    while kolejka:
        u=kolejka.popleft()
        for v in G[u]:
            if not visited[v]:
                visited[v]=True
                parent[v]=u
                path_len[v]=path_len[u]+1
                kolejka.append(v)
    
