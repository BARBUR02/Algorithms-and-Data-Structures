#bottom up
def knapsack(W,P,n):
    l=len(W)
    dp=[[0 for _ in range(n+1) ] for _ in range(len(W)+1)] 
    for i in range(l+1):
        for j in range(n+1):
            if i==0 or j==0:
                dp[i][j]=0
            if W[i-1]<j:
                dp[i][j]=max(dp[i-1][j-W[i-1]]+P[i-1],dp[i-1][j])
    return dp[l][n]

def rek_knap(W,P,i,b,dp):
    if i==0 or b==0:
        return 0
    if dp[i][b]!=None:
        return dp[i][b]
    

    # if b<0:
        # return 0
    if W[i-1]<=b:
        dp[i][b]=max(rek_knap(W,P,i-1,b,dp),rek_knap(W,P,i-1,b-W[i-1],dp)+ P[i-1] )
    else:
        dp[i][b]=rek_knap(W,P,i-1,b,dp)
    return dp[i][b]
W=[2,5,8,12,14,1,3,16,20,21]
P=[6,15,25,8,3,1,20,4,3,2]
dp=[[None for _ in range (36 ) ]for _ in range(len(W)+1)]
print(knapsack(W,P,35))
print(rek_knap(W,P,len(W)-1,35,dp))