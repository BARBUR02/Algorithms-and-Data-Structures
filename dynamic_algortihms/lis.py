def lis(A):
    dp=[0 for _ in range(len(A))]
    record=[-1 for _ in range(len(A))]
    dp[0]=1
    maxi=0
    for i in range(1,len(A)):
        maximum=0
        for j in range(i):
            if A[j]<A[i]:
                # maximum=max(dp[j],maximum)
                if dp[j]>maximum:
                    maximum=dp[j]
                    record[i]=j
        dp[i]=maximum+1
        if dp[i]>dp[maxi]:
            maxi=i
    printsol(A,record,maxi)
    print()

    return max(dp)

def printsol(A,P,i):
    if P[i]!=-1:
        printsol(A,P,P[i])
    print(A[i],end=" ")


tab=[2,1,4,3,4,8,5,7,2,0]
print(lis(tab))