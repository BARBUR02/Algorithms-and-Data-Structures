def insertion(tab):
    n=len(tab)
    for i in range(1,n):
        val=tab[i]
        j=i-1
        while j>=0 and tab[j]>val:
            tab[j+1]=tab[j]
            j-=1
        tab[j+1]=val
    return tab

def bucket_sort(A):
    buckets=[[] for _ in range(10)]
    for el in A:
        index=int(el*10)
        buckets[index].append(el)
    for bucket in buckets:
        bucket=insertion(bucket)
    p=0
    for i in range(len(buckets)):
        for k in range(len(buckets[i])):
            A[p]=buckets[i][k]
            p+=1

A=[0.12,0.22,0.65,0.89,0.97,0.01,0.76,0.46,0.78,0.45,0.49]
bucket_sort(A)
for el in A:
    print(el,end=" ")