def binsearch(A,i,j,key):
    while j-i>1:
        mid=i+(j-i)//2
        if A[mid]>=key:
            j=mid
        else:
            i=mid
    return mid
# def binsearchleft(A,i,j,key):
    

def lis(A):
    n=len(A)
    dp=[0 for _ in range(n)]
    dp[0]=A[0]
    length=1
    for i in range(1,n):
        if A[0]>A[i]:
            dp[0]=A[i]
        elif A[length-1]<A[i]:
            dp[length]=A[i]
            length+=1
            print(dp)
        else:
            index=binsearch(dp,0,length-1,A[i])
            dp[index]=A[i]
    print(dp)
    return length

A=[13,7,21,42,8,2,44,53]
            
print(lis(A))

B=[18,20]
print(len(B))
print(binsearch(B,-1,len(B)-1,19))