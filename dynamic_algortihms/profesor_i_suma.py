def minimize(A,s,e,dp):
    if dp[s][e]!=-1:
        return dp[s][e]
    if abs(e-s)==1:
        return abs(A[s]+A[e])
    result=-1
    for i in range(s+1,e-1):
        left=minimize(A,s,i,dp)
        right=minimize(A,i+1,e,dp)
        result=max(result,abs(left+right))        
    dp[s][e]=result
    return result