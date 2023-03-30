def tower(A):
    maxiind=0
    n=len(A)
    dp=[0 for _ in range(n+1)]
    dp[0]=1
    for i in range(1,n):
        maxi=0
        for j in range(i):
            if inside(A[j],A[i]):
                maxi=max(maxi,dp[j])
        dp[i]=maxi+1
        if dp[i]>dp[maxiind]:
            maxiind=i
    return dp[maxiind]

def inside(A,B):
    if A[0]<=B[0] and A[1]>=B[1]:
        return True
    return False


A=[(1,4),(0,5),(1,5),(2,6),(2,4)]
B=[(10,15),(8,14),(1,6),(3,10),(8,11),(6,15)]
print(tower(A))
print(tower(B))