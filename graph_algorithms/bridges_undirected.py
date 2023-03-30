def bridges(G):
    def bridgeDFS(G,v,visited,parent,low,d):
        nonlocal time
        d[v]=time
        visited[v]=True
        time+=1
        for u in G[v]:
            if not visited[u]:
                parent[u]=v
                bridgeDFS(G,u,visited,parent,low,d)

                low[v]=min(low[v],low[u])
                
                if low[u]>d[v]:
                    print(" (",v,",",u,") ")
            elif v!=parent[u]:
                low[v]=min(low[v],d[u])


    time=1
    n=len(G)
    visited=[False for _ in range(n)]
    d=[float("inf ") for _ in range(n)]
    low=[float("inf ") for _ in range(n)]
    parent=[ None for _ in range(n)]
    for i in range(n):
        if not visited[i]:
            bridgeDFS(G,i,visited,parent,low,d)


G1=[[2,3],
[0],
[1],
[4],
[]]
bridges(G1)
G2=[[1],
[2],
[3],
[]]
print(" \nkolejny :")
bridges(G2)