#Dp Approach
'''def lcs(X, Y): 
    # find the length of the strings 
    m = len(X) 
    n = len(Y) 
  
    # declaring the array for storing the dp values 
    L = [[None]*(n + 1) for i in range(m + 1)] 
  
    """Following steps build L[m + 1][n + 1] in bottom up fashion 
    Note: L[i][j] contains length of LCS of X[0..i-1] 
    and Y[0..j-1]"""
    for i in range(m + 1): 
        for j in range(n + 1): 
            if i == 0 or j == 0 : 
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1]+1
            else: 
                L[i][j] = max(L[i-1][j], L[i][j-1]) 
  
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1] 
    return L[m][n] 
# end of function lcs 
  
  
# Driver program to test the above function 
X = "AGGTAB"
Y = "GXTXAYB"
print("Length of LCS is ", lcs(X, Y)) 

'''
#recursive approach

def lcs(X, Y, m, n): 
  
    if m == 0 or n == 0: 
       return 0; 
    elif X[m-1] == Y[n-1]: 
       return 1 + lcs(X, Y, m-1, n-1); 
    else: 
       return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n)); 
lis=[]
def LCS_dp(X,Y,m,n):
    dp=[[None for _ in range(m+1)] for _ in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if i==0 or j==0:
                dp[i][j]=0
            elif X[j-1]==Y[i-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i][j-1],dp[i-1][j])
    i=n
    j=m
    while(i >0 and  j>0):
        if X[j-1]==Y[i-1]:
            lis.append(X[j-1])
            i=i-1
            j=j-1
        else:
            if dp[i-1][j]>dp[i][j-1]:
                i=i-1
            else:
                j=j-1                               
    return dp[n][m]

  
  
# Driver program to test the above function 
X = "AGGTAB"
Y = "GXTXAYB"
print("Length of LCS is ", lcs(X, Y, len(X), len(Y)) )
print("length of LC dp solution",LCS_dp(X,Y,len(X),len(Y)))
print(lis)