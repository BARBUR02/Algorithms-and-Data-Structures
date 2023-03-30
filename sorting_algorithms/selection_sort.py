def selection_sort(A):
    n=len(A)
    for i in range(n):
        min=A[i]
        index=i
        for j in range(i+1,n):
            if A[j]<min:
                min=A[j]
                index=j
        A[i],A[index]=A[index],A[i]
    return A

tab=[2,5,2,22,77,89,4,3,15,19,11,2213,22]
tab=selection_sort(tab)
for el in tab:
    print( el, end=" ")