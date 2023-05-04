def SCS(X,Y):
    x=len(X)
    y=len(Y)
    dp=[[None for _ in range(y+1)] for _ in range(x+1)]
    for i in range(x+1):
        for j in range(y+1):
            if i==0 or j==0:
                dp[i][j]=0
            elif X[i-1]==Y[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i][j-1],dp[i-1][j])
    i=x
    j=y
    lis=[]
    while(i>0 and j>0):
        if X[i-1]==Y[j-1]:
            lis.append(X[i-1]) 
            i-=1
            j-=1
        else:
            if dp[i-1][j]>dp[i][j-1]:
                lis.append(X[i-1])
                i-=1
            else:
                lis.append(Y[j-1])
                j-=1  
    while(i>0):
        lis.append(X[i-1])
        i-=1
    while(j>0):
        lis.append(Y[j-1])
        j-=1                
                         
    return lis
X = "AGGTAB"
Y = "GXTXAYB"            
l=SCS(X,Y)
l.reverse()
print(l)