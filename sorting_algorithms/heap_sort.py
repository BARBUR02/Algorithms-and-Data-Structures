def parent(i):
    return i//2
def left(i):
    return 2*i+1
def right(i):
    return 2*i+2

def heapify(A,n,i):
    l=left(i)
    r=right(i)
    max_ind=i
    if l<n and A[l]>A[max_ind]:
        max_ind=l
    if r<n and A[r]>A[max_ind]:
        max_ind=r
    if max_ind!=i:
        A[i],A[max_ind]=A[max_ind],A[i]
        heapify(A,n,max_ind)

def build_heap(A):
    n=len(A)
    for i in range(parent(n-1),-1,-1):
    # for i in range(n-1,parent(n),-1):
        heapify(A,n,i)
def heap_sort(A):
    n=len(A)
    build_heap(A)
    for i in range(n-1,0,-1):
        A[i],A[0]=A[0],A[i]
        heapify(A,i,0)



tab=[2,5,2,22,77,89,4,3,15,19,11,2213,22]
heap_sort(tab)
for el in tab:
    print( el, end=" ")
print("sprawdzamy")
print([i for i in range(6,-1,-1)])
# print([i for i in range(-1,6,-1)])