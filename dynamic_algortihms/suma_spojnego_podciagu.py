def maxisum(A):
    n=len(A)
    dp=[1 for _ in range(n)]
    wynik=[0 for _ in range(n)]
    wynik[0]=A[0]
    for i in range(1,n):
        wynik[i]=max(wynik[i-1]+A[i],A[i])
    print(wynik)
    return max(wynik)

dane=[1,3,-7,-2,1,9,-3,2,-100,4]
print(maxisum(dane))