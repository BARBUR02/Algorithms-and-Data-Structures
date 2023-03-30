def zbigniew(A,i,e,dp):
    if i==len(A)-1:
        return 0
    if dp[e][i]!=-1:
        return dp[e][i]
    minimum=float("inf")
    for k in range(1,e+1):
        if i+k>=len(A):
            break
        minimum=min(minimum,zbigniew(A,i+k,e-k+A[i+k],dp)+1)
    dp[e][i]=minimum
    return dp[e][i]



A=[4,5,2,4,1,2,1,0]
B=[2,2,1,0,0,0]
suma=sum(A)
# print(suma)
sumb=sum(B)
dpa=[[-1 for _ in range(len(A))] for _ in range(suma)]
dpb=[[-1 for _ in range(len(B))] for _ in range(sumb)]
print(zbigniew(A,0,A[0],dpa))
print(zbigniew(B,0,B[0],dpb))