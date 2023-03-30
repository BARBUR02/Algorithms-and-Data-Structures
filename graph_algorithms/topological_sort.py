from collections import deque
def topological_sort(G):
    def DFS_util(G,v,visited,result):
        visited[v]=True
        for u in G[v]:
            if not visited[u]:
                DFS_util(G,u,visited,result)
        result.appendleft(v)
    n=len(G)
    visited=[False for _ in range(n)]
    result=deque()
    for v in range(n):
        if not visited[v]:
            DFS_util(G,v,visited,result)
    print(list(result))

G=[[],
    [],
    [3],
    [1],
    [4,1],
    [2,0]
]
topological_sort(G)