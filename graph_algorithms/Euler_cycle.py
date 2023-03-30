from collections import deque



def Euler(G):
    def DfSEuler(G,vertex,visited,result):
        # result.append(vertex)
        for v in G[vertex]:
            if not visited[vertex][v]:
                visited[vertex][v]=True
                visited[v][vertex]=True
                result=DfSEuler(G,v,visited,result)
                result.appendleft(vertex)
        return result

    n=len(G)
    result=deque()
    visited=[[False for _ in range(n)] for _ in range(n)]
    cycle=DfSEuler(G,0,visited,result)
    print(result)
    print(cycle)
    # for v in range(n):
    #     for u in range(G[v]):
    #         visited[v][u]=visited[u][v]=True
    

G=[
 [1,2,3],
 [0,2],
 [0,1],
 [0,4],
 [0,3]   
]
Euler(G)