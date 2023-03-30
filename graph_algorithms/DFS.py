def DFS(G):
    def DFS_util(G,v,visited,parent):
        nonlocal time
        time+=1
        timetable[v]=time
        visited[v]=True
        for u in G[v]:
            if not visited[u]:
                # visited[u]=True
                parent[u]=v
                DFS_util(G,u,visited,parent)
        time+=1
        
    n=len(G)
    time=0
    visited=[False for _ in range(n)]
    parent=[None for _ in range(n)]
    timetable=[0 for _ in range(n)]
    for i in range(n):
        if not visited[i]:
            DFS_util(G,i,visited,parent)
    print(timetable)
    print(time)

G=[ [2,3],
    [0,1],
    [4],
    [1,2],
    [2,3,1]
]
DFS(G)