def lcs(X,Y,n1,n2):
    if n1==-1 or n2==-1:
        return 0
    if X[n1]==Y[n2]:
        return lcs(X,Y,n1-1,n2-1)+1
    else:
        return max(lcs(X,Y,n1-1,n2),lcs(X,Y,n1,n2-1))

def lcs_v2(X,Y,m,n,dp):
    if m==0 or n==0:
        return 0
    if dp[m][n]!=-1:
        return dp[m][n]
    if X[m-1]==Y[n-1]:
        dp[m][n]= 1+ lcs_v2(X,Y,m-1,n-1,dp)
        return dp[m][n]
    dp[m][n]=max(lcs_v2(X,Y,m,n-1,dp),lcs_v2(X,Y,m-1,n,dp))
    return dp[m][n]

X="AGGTAB"
Y="GXTXAYB"
n=len(Y)
m=len(X)
dp=[[-1 for _ in range(n+1)] for _ in range(n+1)]
print(lcs(X,Y,len(X)-1,len(Y)-1))
print(lcs_v2(X,Y,m,n,dp))