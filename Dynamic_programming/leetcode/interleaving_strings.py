#task- given- 3 strings s1, s2, s3, check whether s3 is formed by mixing s1 ans s2 in order
# approach- start comparing last chars of both s1 and s2 with that of s3, there is decision in decision tree
#           1. s1[last] = s3[last], so check for s1[last-1], s3[last-1], s2, i.e current char of s3 came from s1
#           2. s2[last] = s3[last], so check for s2[last-1], s3[last-1], s1, i.e current char of s3 came from s2
#           return option1 || option2
# memoize in dp, to reduce complexity
global dp
def solve(s1,s2,s3,i,j,k):
        global dp
        # if s3 charcters are completed, i.e all char of s3 are covered by s1 amd s2, return True
        if k==0:
            return True
        
        if dp[i][j]!=-1:
            return dp[i][j]
        first=False
        second=False

        #condition 1- if curr char part of s1
        if i>0 and s3[k-1]==s1[i-1]:
            first=solve(s1,s2,s3,i-1,j,k-1)
        #condition 2- if curr char part of s2
        if j>0 and s3[k-1]==s2[j-1]:
            second=solve(s1,s2,s3,i,j-1,k-1)
            
        dp[i][j]=first or second
        return dp[i][j]
        
        
def isInterleave(s1: str, s2: str, s3: str) -> bool:
        global dp
        i=len(s1)
        j=len(s2)
        k=len(s3)
        dp=[[-1 for _ in range(j+1)] for _ in range(i+1)]

        # if sum of len of both s1 and s2 is not equal s3, hence s3 is nt interleaved string
        if i+j!=k:
            return False
        return solve(s1,s2, s3, i,j,k)
s1="aabcc"
s2="dbbca"
s3="aadbbcbcac"
print(isInterleave(s1,s2,s3))