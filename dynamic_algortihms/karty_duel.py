def karty_duel(A,a,b,dp):
    if dp[a][b]!=None:
        print("yass: ",a,b,dp[a][b])
        return dp[a][b]
    if a==b:
        dp[a][a]=A[a]
        return A[a]
    if abs(a-b)==1:
        dp[a][b]=max(A[a],A[b])
        return max(A[a],A[b])
    canda=candb=float("inf")
    if a+2<=b:
        canda=min(karty_duel(A,a+2,b,dp)+A[a],karty_duel(A,a+1,b-1,dp)+A[a])
    if b-2>=a:
        candb=min(A[b]+karty_duel(A,a,b-2,dp),A[b]+karty_duel(A,a+1,b-1,dp))
    if canda==float("inf") or candb==float("inf"):
        res=min(canda,candb)
        if res==float("inf"):
            res=0
    else:
        res=max(canda,candb)
    dp[a][b]=res
    return res

# A=[1,5,4,1,2,7,8,4]
A=[1,5,2,4,6]
n=len(A)
dp=[[None for _ in range(n)] for _ in range(n)]
print(karty_duel(A,0,len(A)-1,dp))