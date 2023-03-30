def quicksort(A,p,r):
    if p<r:
        q=partition(A,p,r)
        quicksort(A,p,q)
        quicksort(A,q+1,r)
def partition(A,p,r):
    pivot=A[p]
    i=p-1
    j=r+1
    while True:
        i+=1
        while A[i]<pivot:
            i+=1
        j-=1
        while A[j]>pivot:
            j-=1
        if i>=j:
            return j
        A[i],A[j]=A[j],A[i]


tab=[2,5,2,22,77,89,4,3,15,19,11,2213,22]
quicksort(tab,0,len(tab)-1)
for el in tab:
    print( el, end=" ")





