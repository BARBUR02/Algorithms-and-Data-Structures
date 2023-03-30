def radix_sort(A):
    max1=max(A)

    exp=1
    while max1/exp>1:
        counting_sort(A,lambda x: (x//exp)%10)
        exp*=10

def counting_sort(A,f):
    n=len(A)

    output=[0 for _ in range(n)]
    count=[0 for _ in range(10)]

    for i in range(n):
        index=f(A[i])
        count[index]+=1
    for i in range(1,10):
        count[i]+=count[i-1]

    i=n-1
    while i>=0:
        index=f(A[i])
        output[count[index]-1]=A[i]
        count[index] -=1
        i-=1

    for i in range(0,len(A)):
        A[i]=output[i]

tab=[12,14,51,62,13,62,15,97,80]
radix_sort(tab)
for el in tab:
    print(el,end=" ")
