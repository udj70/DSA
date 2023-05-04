# task- find NGR in circular array, NGR is -1 if NGR not exist
# approach- find greater element in array, now NGR of this elemnt will always be non exisiting, start from this element, 
# and move left ward in circular manner, and come back to greatest element and break loop
# dry run to better understand
class Solution:
    def nextGreaterElements(self, nums):
        ngr=[-1]*len(nums)
        mx=float('-inf')
        mx_index=-1
        for i in range(len(nums)):
            if nums[i]>=mx:
                mx=nums[i]
                mx_index=i
        j=mx_index-1
        stack=[]
        stack.append(nums[mx_index])
        while(j!=mx_index):
            while(len(stack) and nums[j]>=stack[-1]):
                stack.pop()
            if len(stack):
                ngr[j]=stack[-1]
            stack.append(nums[j])
            j=(j-1+len(nums))%len(nums)
        return ngr        