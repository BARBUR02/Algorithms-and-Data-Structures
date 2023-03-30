def sumequal(T,sum):
    n=len(T)
    dp=[[False for _ in range(sum+1)] for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0]=True
        if i==T[0]:
            dp[0][i]==True
    for i in range(1,n+1):
        for j in range(sum+1):
            if T[i-1]<=sum:
                dp[i][j]=dp[i-1][j] or dp[i-1][j-T[i-1]]
            else:
                dp[i][j]=dp[i-1][j]
    # print(dp)
    for el in dp:
        print(el)


T=[1,5,7,14,3,2,9]
sumequal(T,8)