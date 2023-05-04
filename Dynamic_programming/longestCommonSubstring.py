def LCSubstring(X,Y,m,n):
    dp=[[None for _ in range(n+1)] for _ in range(m+1)]
    ma=0
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                dp[i][j]=0
            elif X[i-1]==Y[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:    
                dp[i][j]=0
            if dp[i][j]>ma:
                ma=dp[i][j]                      
    #print(dp)
    return ma
X="abcedf"
Y="akbcedyz"
print(LCSubstring(X,Y,len(X),len(Y)))   
#maintain global count             
global count
def LCSrecursive(X,Y,c):
    global count
    if len(X)==0 or len(Y)==0:
        return 
    elif X[-1]==Y[-1]:
        #pass incremented count in third parameter
        LCSrecursive(X[:len(X)-1],Y[:len(Y)-1],c+1)
    else:
        #pass 0 in count
        #update global count 
        count=max(count,c)
        LCSrecursive(X,Y[:len(Y)-1],0)
        LCSrecursive(X[:len(X)-1],Y,0)    
count=0
LCSrecursive(X,Y,0)# updated third variable as count, becuse as off now recursive approach same is dp is not found
print(count)