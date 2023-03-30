def sumequality(A,n,i,dp):
    if n<0:
        return False
    if n==0:
        return True
    if i<0:
        return False
    if dp[n][i][0]:
        return dp[n][i][1]
    dp[n][i][0]=True
    dp[n][i][1]=sumequality(A,n-A[i],i-1,dp) or sumequality(A,n,i-1,dp)
    return dp[n][i][1]
A=[6,4,2,1,-6,9,12,14]
l=len(A)
n=-4
dp=[[[False,False] for _ in range(l)] for _ in range(n+1)]
print(sumequality(A,n,len(A)-1,dp))