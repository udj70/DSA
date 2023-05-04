# task- check leetcode probelm statement
# approach- 4 case-> 1. string start with 0, no decoding possible
#                        2. string start with 1, consider 1 number, check in remaing or consider first 2 num, check in remaining
#                        3. string start with 2, consider 1 number, check in remianing or consider first 2 number if second number is less that 6, and check in remaining
#                        4. else if string start with 3-9, then can consider only first number, check in remaining
#top down memoization approach
class Solution:
    def solve(self,S,i,dp):
          if i==len(S):
            return 1
          if dp[i]!=-1:
            return dp[i]
          if S[i]=='0':
            return 0
          elif S[i]=='1':

            one=self.solve(S,i+1,dp)
            two=self.solve(S,i+2,dp) if i+2<=len(S) else 0
            dp[i]=one+two
            return dp[i]
          elif S[i]=='2':
            one=self.solve(S,i+1,dp)
            two=self.solve(S,i+2,dp) if (i+2<=len(S) and int(S[i+1])<=6) else 0
            dp[i]=one+two
            return dp[i]
          else:
            dp[i]=self.solve(S,i+1,dp)
            return dp[i]

            
    def numDecodings(self, s: str) -> int:
        dp=[-1]*(len(s)+1)
        return self.solve(s,0,dp)
            
s=Solution()
print(s.numDecodings("226")) #3-  2 2 6, 22 6, 2 26


#bottom up dp approach
# incorrect code
def decode_ways(s):
    if len(s)==0:
        return 0
    dp=[0]*(len(s)+1)
    dp[len(s)]=1

   
    for i in range(len(s)-1,-1,-1):

        if s[i]=="0":
            dp[i]=0
        elif s[i]=="1":
            dp[i]=dp[i+1]+(dp[i+2] if i+2<len(s)+1 else 0)
        elif s[i]=="2":
            dp[i]=dp[i+1]+(dp[i+2] if i+2<(len(s)+1) and s[i+1]<="6" else 0)
        else:
            dp[i]=dp[i+1]
        #print(dp)
    return dp[0]

print(decode_ways("226"))


