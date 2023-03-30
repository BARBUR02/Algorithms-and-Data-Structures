def counting_sort(A):
    n=len(A)
    B=[0 for _ in range(n)]
    maximum=A[0]
    for el in A:
        if el>maximum:
            maximum=el
    C=[0 for _ in range(maximum+1)]
    for el in A:
        C[el]+=1
    for i in range(1,maximum+1):
        C[i]+=C[i-1]
    for i in range(n-1,-1,-1):
        B[C[A[i]]-1]=A[i]
        C[A[i]]-=1
    for i in range(n):
        A[i]=B[i]

tab=[2,4,3,1,6,7,8,9,10,11,12,14,15,16,13,13]
counting_sort(tab)
for el in tab:
    print ( el, end=" ")