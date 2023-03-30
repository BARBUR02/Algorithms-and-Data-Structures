def Coins(coins, m ,V,dp):
    if V==0:
        return 0
    if dp[V]!=None:
        # print("done")
        return dp[V]
    minimum=float("inf")
    for i in range(m):
        if coins[i]<=V:
            minimum=min(minimum,Coins(coins,m,V-coins[i],dp)+1)
    # minimum+=1
    if dp[V]!=float("inf"):
        dp[V]=minimum
    return dp[V]

def bottom_up(coins,V):
    n=len(coins)
    dp=[0 for _ in range(V+1)]
    for i in range(1,V+1):
        minimum=float("inf")
        for j in range(n):
            if coins[j]<=i:
                minimum=min(minimum,dp[i-coins[j]])
        dp[i]=minimum+1
    return dp[V]




coins=[1,6,5,9]
m=len(coins)
V=22
dp=[None for _ in range(V+1)]
print(Coins(coins,m,V,dp))
print(bottom_up(coins,V))