def intuse(I,x,y):
    T=enumerate(I)
    T=[(value,index) for index,value in T]
    T.sort(key=lambda x: x[0][0])
    print(T)
    dp=[[[None,[]] for _ in range (y-x+1) ]for _ in range(len(T)+1) ]
    print( solve(T,x,y,0,dp))
    for el in dp:
        print(el)
    result=[]
    for i in range(len(T)+1):
        for j in range(y-x+1):
            if dp[i][j][0] and dp[i][j][1]:
                result.append(dp[i][j][1])
    return result

def solve(T,x,y,i,dp):
    if y==x:
        return True
    if dp[i][y-x][0]!=None:
        print("done")
        return dp[i][y-x][0]
    if i>=len(T):
        return False
    if T[i][0][0]>x:
        return False
    val=False
    if T[i][0][0]==x and T[i][0][1]<=y:
        val=solve(T,T[i][0][1],y,i+1,dp) #or solve(T,x,y,i+1,dp)
        if val:
            dp[i][y-x][1].append(T[i][1])
    comp=solve(T,x,y,i+1,dp)
    dp[i][y-x][0]=  comp or val
    return dp[i][y-x][0]

     

dane=[(3,4),(2,9),(1,3),(4,6),(1,4),(2,4),(1,2),(1,6),(1,7),(2,6)]
print(intuse(dane,1,6))
