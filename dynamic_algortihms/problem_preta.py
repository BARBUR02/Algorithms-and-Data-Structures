def memoized_cut_rod(A,dp,n):
    if dp[n]!=None:
        return dp[n]
    if n==0:
        dp[n]=0
        return 0
    maximum=-1
    for i in range(1,n+1):
        maximum=max(maximum,memoized_cut_rod(A,dp,n-i)+A[i-1])
    dp[n]=maximum
    return dp[n]

#bottom_up
def bottom_up(A,n):
    best_to_len=[0 for _ in range(n+1)]
    par=[None for _ in range(n+1)]
    for i in range(1,n+1):
        maximum=best_to_len[i]
        for j in range(i):
            # maximum=max(maximum,A[j]+best_to_len[i-j-1])
            if A[j]+best_to_len[i-j-1]>maximum:
                par[i]=j+1
                maximum=A[j]+best_to_len[i-j-1]
        best_to_len[i]=maximum
    # for el in best_to_len:
    # print(best_to_len)
    result=n
    while par[n]!=None:
        print(par[n],end=" ")
        n-=par[n]
    print()
    return best_to_len[result]



cennik=[1,5,8,9,10,17,17,20,24,30]
n=9
dp=[None for _ in range(n+1)]
print(memoized_cut_rod(cennik,dp,n))
print("2 podejscie: ")
print(bottom_up(cennik,n))
