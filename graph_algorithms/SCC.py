def SSC(G):
    def fillorder(G,v,visited,order):
        for u in G[v]:
            if not visited [u]:
                visited[u]=True
                fillorder(G,u,visited,order)
        order.append(v)
    def DFS(G,v,visited):
        visited[v]=True
        print(v,end=" ")
        for u in G[v]:
            if not visited[u]:
                visited[u]=True
                DFS(G,u,visited)
    def Trasposition(G):
        n=len(G)
        result=[[] for _ in range(n)]
        for u in range(n):
            for v in G[u]:
                result[v].append(u)
        return result
    n=len(G)
    stack=[]
    visited=[False for _ in range(n)]
    for i in range(n):
        if visited[i]==False:
            fillorder(G,i,visited,stack)
    graph=Trasposition(G)
    visited=[False for _ in range(n)]
    print(stack)
    while stack:
        u=stack.pop()
        if not visited[u]:
            print()
            DFS(graph,u,visited)


G=[[2,3],
[0],
[1],
[4],
[]
]
SSC(G)