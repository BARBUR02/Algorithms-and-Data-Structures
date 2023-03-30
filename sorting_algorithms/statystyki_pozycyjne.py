def select(A,p,k,r):
    if p==r:
        return A[p]
    if p<r:
        q=partition(A,p,r)
    if q==k: return A[q]
    elif q<k: return select(A,q+1,k,r)
    else:   return select(A,p,k,q-1)

def partition(A,p,r):
    x=A[r]
    i=p-1
    for j in range(p,r):
        if A[j]<=x:
            i+=1
            A[i],A[j]=A[j],A[i] 
    A[i+1],A[r]=A[r],A[i+1]
    return i+1

tab=[2,5,2,22,77,89,4,3,15,19,11,2213,22]
print(select(tab,0,len(tab),len(tab)-1))
# for el in tab:
#     print( el, end=" ")
T=[[2,3,5],
    [7,11,13],
    [17,19,23]
    ]
# n=len(T)
# A=[T[i//n][i%n] for i in range(n*n)]
# print(select(A,0,3,n*n-1) )
# print(ord('a'),ord('b'),ord('z'))