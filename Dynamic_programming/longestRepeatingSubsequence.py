def LRS(X):
    x=len(X)
    dp=[[None for _ in range(x+1)] for _ in range(x+1)]
    for i in range(x+1):
        for j in range(x+1):
            if i==0 or j==0:
                dp[i][j]=0
            elif X[i-1]==X[j-1] and i!=j:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i][j-1],dp[i-1][j])
    i=x
    j=x 
    s=""
    while(i>0 and j>0):
        if dp[i][j]==dp[i-1][j-1]+1:
            s=s+X[i-1]
            i-=1
            j-=1
        elif dp[i][j]==dp[i-1][j]:
            i-=1
        else:
            j-=1                   
    return s,dp[x][x]
X="AABEBCDD"
s,l=LRS(X)
s=''.join(reversed(s))
print("LRS of X is",s,"of length",l)                       