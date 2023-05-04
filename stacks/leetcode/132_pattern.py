# task- given integer array, find 132 pattern can be formed, i.e nums[i]<nums[j]>nums[k] and nums[k]>nums[i]

# approach- find second largest in right , while popping element in calculating NGR, just save popped value in variable, last popped element will be second largest
#           check at avery i , if nums[i]<secondMax, return True
class Solution:
    def find132pattern(self, nums):
        secondMax=float('-inf')
        n=len(nums)
        stack=[nums[n-1]]
        for i in range(n-2,-1,-1):
            if nums[i]<secondMax:
                return True
            while(len(stack) and nums[i]>stack[-1]):
                secondMax=stack.pop()
            stack.append(nums[i])
        return False
s=Solution()
print(s.find132pattern([1,4,2,3,4,5])) # 1,4,2