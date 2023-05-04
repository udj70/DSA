'''
A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= nums[j]. The width of such a ramp is j - i.

Given an integer array nums, return the maximum width of a ramp in nums. If there is no ramp in nums, return 0.

 

Example 1:

Input: nums = [6,0,8,2,1,5]
Output: 4
Explanation: The maximum width ramp is achieved at (i, j) = (1, 5): nums[1] = 0 and nums[5] = 5.
Example 2:

Input: nums = [9,8,1,0,1,9,4,0,4,1]
Output: 7
Explanation: The maximum width ramp is achieved at (i, j) = (2, 9): nums[2] = 1 and nums[9] = 1.
'''
# approach- best- use decreasing stack- push index if current element is less that stack top, else check smaller in stack, which is at most left position in stack by binary search
#           tc- O(N*logN) sc=O(N)



class Solution:
    def findsmaller(self,start,end,stack,nums,ref_idx):
        potential_ans=-1
        while(start<=end):
            mid=start+(end-start)//2
            if nums[stack[mid]]<=nums[ref_idx]:
                potential_ans=mid
                end=mid-1
            else:
                start=mid+1
        return stack[potential_ans]
    def maxWidthRamp(self, nums):
        stack=[0]
        ans=0
        for i in range(1,len(nums)):
            if nums[i]<nums[stack[-1]]:
                stack.append(i)
            else:
                idx=self.findsmaller(0,len(stack)-1,stack,nums,i)
                ans=max(ans,i-idx)
                #print(idx,i)
            #print(stack)
        return ans

s=Solution()
nums=[6,0,8,2,1,5]
print(s.maxWidthRamp(nums)) #4