
def LPS_DP(seq,i,j):
    l=j-i+1
    dp=[[0 for _ in range(l)] for _ in range(l)]
    for n in range(l):
        dp[n][n]=1
    for cl in range(2,l+1):#LPS for substring of len 2,3,4...i.e maintaining const. diff b/w and m of length cl
        for n in range(l-cl+1):
            m=n+cl-1
            if seq[n]==seq[m] and cl==2:
                dp[n][m]=2
            elif seq[n]==seq[m]:
                dp[n][m]=dp[n+1][m-1]+2
            else:
                dp[n][m]=max(dp[n+1][m],dp[n][m-1])
    return dp[0][l-1]            



def LPS_Recursive(seq,i,j):
    if i==j:
        return 1
    if seq[i]==seq[j] and i+1==j:
        return 2
    if seq[i]==seq[j] and i+1!=j:
        return LPS_Recursive(seq,i+1,j-1)+2
    return max(LPS_Recursive(seq,i+1,j),LPS_Recursive(seq,i,j-1))
arr=[1,2,3,2,3,4,5,3,5,2,1]
print(LPS_Recursive(arr,0,len(arr)-1))   #[1,2,3,4,3,2,1] length=5 
print(LPS_DP(arr,0,len(arr)-1))

#or simply find LCS of given string with its reverse


