def matrioszki(A):
    n=len(A)
    A.sort(key=lambda x: x[0])
    dp=[None for _ in range(n)]
    def solve(A,i,dp):
        if i==-1:
            return 0
        if dp[i] is not None:
            return dp[i]
        maxi=-1
        for k in range(i+1,n):
            maxi=max(maxi,solve(A,k,dp)+1)
