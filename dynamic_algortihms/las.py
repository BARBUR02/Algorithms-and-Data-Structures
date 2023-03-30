def forest(A):
    dp=[0 for _ in range(len(A))]
    dp[0]=A[0]
    dp[1]=max(A[0],A[1])
    for i in range(2,len(A)):
        dp[i]=max(dp[i-1],dp[i-2]+A[i])
    return dp[len(A)-1]




A=[7,2,5,4,3,9,2]
print(forest(A))