def AP(G):
    def APdfs(G,v,visited,d,parent,low,ap):
        nonlocal time
        d[v]=time
        low[v]=time
        time+=1
        visited[v]=True
        children=0

        for u in G[v]:
            if not visited[u]:
                parent[u]=v
                children+=1
                APdfs(G,u,visited,d,parent,low,ap)

                low[v]=min(low[u],low[v])

                if parent[v]==None and children>1:
                    ap[v]=True

                if parent[v]!=None and low[u]>=d[v]:
                    ap[v]=True 
            elif v!=parent[u]:
                low[v]=min(low[v],d[u])
    
    time=1
    n=len(G)
    visited=[False for _ in range(n)]
    d=[float("inf") for _ in range(n)]
    low=[float("inf ") for _ in range(n)]
    parent=[None for _ in range(n)]
    ap=[False for _ in range(n)]

    for v in range(n):
        if not visited[v]:
            APdfs(G,v,visited,d,parent,low,ap)
    print("articulation points: ")
    for index,value in enumerate(ap):
        if value==True:
            print(index, end=" ")


G=[[2,3],
[0],
[1],
[4],
[]]

AP(G)