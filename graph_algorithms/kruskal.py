#listy:
# class Node:
#     def __init__(self,value):
#         self.parent=self
#         self.value=value
#         self.rank=0
# def find(x): 
#     if x.parent!=x:
#         x.parent=find(x.parent)
#     return x.parent
# def union(x,y):
#     x=find(x)
#     y=find(y)
#     if x==y:
#         return
#     if x.rank>y.rank:
#         y.parent=x
#     else:
#         x.parent=y
#         if x.rank==y.rank:
#             y.rank+=1


#tablice:
def find(parent,x):
    while parent[x]!=x:
        parent[x]=find(parent,parent[x])
    return x
def union(parent,rank,x,y):
    x=find(parent,x)
    y=find(parent,y)
    if rank[x]<rank[y]:
        parent[x]=y
    elif rank[x]>rank[y]:
        parent[y]=x
    else:
        parent[y]=x
        rank[x]+=1


def Kruskal(G):
    n=len(G)
    G.sort(key=lambda x:x[1]) #zakladam postac[(v,u),w]
    # separate=[Node(i) for i in range(n)]
    parent=[i for i in range(n)]
    rank=[0 for _ in range(n)]
    # rank=[]
    counter=1
    i=0
    result=[]
    while counter <= n-1:
        u,v,w=G[i]
        i+=1
        x=find(parent,x)
        y=find(parent,u)
        if x!=y:
            counter+=1
            result.append((u,v,w))
            union(parent,rank,x,y)