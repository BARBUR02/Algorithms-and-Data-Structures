def MergeSort(tab):
    if len(tab)>1:
        mid=len(tab)//2
        L=tab[:mid]
        R=tab[mid:]

        MergeSort(L)
        MergeSort(R)

        merge(tab,L,R)
def merge(tab,L,R):
    n1=len(L)
    n2=len(R)
    i=j=k=0
    while i<n1 and j<n2:
        if L[i]<R[j]:
            tab[k]=L[i]
            i+=1
        else:
            tab[k]=R[j]
            j+=1
        k+=1
    while i<n1:
        tab[k]=L[i]
        k+=1
        i+=1
    while j<n2:
        tab[k]=R[j]
        j+=1
        k+=1


tab=[2,5,2,22,77,89,4,3,15,19,11,2213,22]
MergeSort(tab)
for el in tab:
    print( el, end=" ")


        

