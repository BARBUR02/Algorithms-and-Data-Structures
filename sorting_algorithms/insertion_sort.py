def Insertion_sort(tab):
    n=len(tab)
    for i in range(1,n):
        val=tab[i]
        j=i-1
        while val<tab[j] and j>=0:
            tab[j+1]=tab[j]
            j-=1
        tab[j+1]=val
    return tab

tab=[2,5,2,22,77,89,4,3,15,19,11,2213,22]
tab=Insertion_sort(tab)
for el in tab:
    print( el, end=" ")