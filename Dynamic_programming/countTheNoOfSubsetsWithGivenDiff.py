import countNoOfSubsetsWithGivenSum

arr=[1,1,2,3]
#subset1+subset2=sum(arr)---1
#subset1-subset2=givenDiffenrence---2
#solving 1 and 2
#subset1=(diff+sum(arr))//2
#problem reduced to count of subset with given difference
diff=1
subsetSum=(sum(arr)+diff)//2

# this approach will not handle all cases
print(countNoOfSubsetsWithGivenSum.countSubs(arr,subsetSum))



# correct approach

class Solution:
    def findTargetSumWays(self, nums, S):
        index = len(nums) - 1
        curr_sum = 0
        self.memo = {}
        return self.dp(nums, S, index, curr_sum)
        
    def dp(self, nums, target, index, curr_sum):
        if (index, curr_sum) in self.memo:
            return self.memo[(index, curr_sum)]
        
        # if elements are finished, and curr_sum become target sum, return 1
        if index < 0 and curr_sum == target:
            return 1
        if index < 0:
            return 0 
        
        # there are two decision, either pick current element as postive or negative
        positive = self.dp(nums, target, index-1, curr_sum + nums[index])
        negative = self.dp(nums, target, index-1, curr_sum + -nums[index])
        
        self.memo[(index, curr_sum)] = positive + negative
        return self.memo[(index, curr_sum)]
s=Solution()
print(s.findTargetSumWays(arr,diff))