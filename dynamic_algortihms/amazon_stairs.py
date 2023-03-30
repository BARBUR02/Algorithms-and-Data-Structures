def amazon(A):
    n=len(A)
    dp=[0 for _ in range(n)]
    dp[0]=1
    for i in range(n):
        for j in range(A[i]):
            dp[i+j+1]+=dp[i]
    return dp[n-1]


A=[1,3,2,1,1,0]
print(amazon(A))