# task- Given a stcik of len n, and some positions array where we can cut. Find min cost to cut.
#       cost to cut is defined by length of rod we are cutting
#       refer leetcode problem ststement
# approach 1- recursive and memo
#refer striver for explaination
class Solution:
    def solve(self,cuts,i,j,dp):
        # 
        if i>j:
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        mini=float('inf')
        for k in range(i,j+1):

            # current cost is cuts[j+1]- cuts[i-1]
            cost=cuts[j+1]-cuts[i-1]+ self.solve(cuts,i,k-1,dp)+ self.solve(cuts,k+1,j,dp)
            mini=min(mini,cost)
        dp[i][j] = mini
        return mini
        
    def minCost(self, n: int, cuts: List[int]) -> int:
        # make new array, add 0 and max len of stick value in start and end
        new_cuts=[]
        new_cuts.append(0)
        new_cuts=new_cuts[:]+cuts[:]
        new_cuts.append(n)


        l=len(new_cuts)
        # sort new array

        new_cuts.sort()
        dp=[[-1 for _ in range(l)] for _ in range(l)]

        # now solution range will be 1 to len(new_cuts)-2
        return self.solve(new_cuts,1,len(new_cuts)-2,dp)