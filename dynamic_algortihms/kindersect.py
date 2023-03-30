def intersects(left,right,val):
    if val[1]<=left or val[0]>=right:
        return False,None,None
    else:
        return True,max(left,val[0]),min(right,val[1])

def kindersect(A,k):
    T=enumerate(A)
    T=[(value,index) for index,value in T]
    T.sort(key=lambda x: x[0][0])
    print(T)
    dp=[[None for _ in range(k+1)] for _ in range(len(T))]
    par=[ [None for _ in range(k+1)] for _ in range(len(T))]
    # f(T,dp,par,0,k,None,None)
    # for el in dp:
        # print(el)
    print("WYNIK:", dp[0][k])
    return list(range(k))

def f(A,dp,par,i,k,left,right):
    if k==0:
        return right-left
    if i>=len(A):
        return 0
    if left==None:
        if len(A)-i<k:
            return -1
        f2=f(A,dp,par,i+1,k-1,A[i][0][0],A[i][0][1])
        f1=f(A,dp,par,i+1,k,left,right)
        dp[i][k]=max(f1,f2)
        return dp[i][k]
    if dp[i][k]!=None:
        # print("yass")
        return dp[i][k]
    if A[i][0][0]>right:
        return -1

    max1=-1
    val,left_cand,right_cand=intersects(left,right,A[i][0])
    if val:
        max1=f(A,dp,par,i+1,k-1,left_cand,right_cand)
    max2=f(A,dp,par,i+1,k,left,right)
    maxim=max(max1,max2)
    dp[i][k]=maxim
    return dp[i][k]

A=[(0,4),(1,10),(6,7),(2,8),(1,7)]
print(kindersect(A,3))