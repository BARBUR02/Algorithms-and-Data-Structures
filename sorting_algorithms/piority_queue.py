#Cos do czego mozna wstawiac elemnty w dowolnej kolejnosci
# i wyciagac w kolejnosci zgodnej z priorytetem

class Priority_queue:
    def __init__ (self,n):
        self.T=[None for _ in range(n)]
        self.size=0
    def add(self,val):
        self.T[self.size]=val
        heapify_upp(self.T,self.size)
        self.size+=1
    def pop(self):
        T=self.T
        if self.size==0:
            return
        val=T[0]
        T[0]=T[self.size-1]
        self.size-=1
        heapify(T,self.size,0)
        # return val


def parent(i):
    return i//2
def left(i):
    return 2*i+1
def right(i):
    return 2*i+2
def heapify_upp(A,i):
    p=parent(i)
    if p>0:
        if A[p]>A[i]:
            A[i],A[p]=A[p],A[i]
            i=p
            heapify_upp(A,i)
    if p==0:
        if A[p]>A[i]:
            A[p],A[i]=A[i],A[p]
def heapify(A,n,i):
    l=left(i)
    r=right(i)
    min_ind=i
    if l<n and A[l]<A[min_ind]:
        min_ind=l
    if r<n and A[r]<A[min_ind]:
        min_ind=r
    if min_ind!=i:
        A[i],A[min_ind]=A[min_ind],A[i]
        heapify(A,n,min_ind)

def build_min_heap(A):
    n=len(A)
    for i in range(parent(n),-1,-1):
        heapify(A,n,i)
def heap_sort(A):
    n=len(A)
    build_min_heap(A)
    for i in range(n-1,0,-1):
        A[i],A[0]=A[0],A[i]
        heapify(A,i,0)

#wstawianie:

A=Priority_queue(10)
A.add(5)
A.add(8)
A.add(120)
A.add(16)
A.add(23)
A.pop()
A.add(15)
for el in A.T:
    print(el,end= " ")
