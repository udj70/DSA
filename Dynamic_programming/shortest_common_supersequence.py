def LCS(s1,s2,m,n):
    dp=[[-1 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                dp[i][j]=0
            elif s1[i-1]==s2[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp                    
def generateSCS(s1,s2,dp):
    i=len(s1)
    j=len(s2)
    ans=""
    while(i>0 and j>0):
        if s1[i-1] == s2[j-1]:
            ans+=s1[i-1]
            i-=1
            j-=1
        elif dp[i-1][j]>dp[i][j-1]:
            ans+=s1[i-1]#while printing only LCS we never add these elements which are not equal
            i-=1
        else:
            ans+=s2[j-1]
            j-=1
    while(i>0):
        ans+=s1[i-1]
        i-=1
    while(j>0):
        ans+=s2[j-1]
        j-=1            
    return ans            



s1='acbef'
s2='bcdaf'
dp=LCS(s1,s2,len(s1),len(s2))
ans=generateSCS(s1,s2,dp)
print(ans[::-1])