def zaba(i,e,c,computed,n):
    if computed[i][e]:
        print("done", i ,e)
        return computed[i][e]
    elif i==n-1:
        # computed[i][e]=0
        # return computed[i][e]
        return 0
    else:
        minimal=n+1
        for j in range(1,e+1):
            if i+j>=n:
                break
            minimal=min(minimal,zaba(i+j,e-j+c[i+j],c,computed,n))
            # print(minimal)
        if minimal!=n+1:
            computed[i][e]=minimal+1
        else:
            computed[i][e]=0
    return computed[i][e]

dane=[1,2,2,1,1,3,1,1]
e=sum(dane)
help=[[None for _ in range(e)] for _ in range(len(dane))]
print(zaba(0,dane[0],dane,help,len(dane)))