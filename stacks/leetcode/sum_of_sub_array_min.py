'''
Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

 

Example 1:

Input: arr = [3,1,2,4]
Output: 17
Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.

'''
# approach - we know that number of subarray a element can make will be num of elements in its right inclusive,
#           here we have to find min in each sub array, so starting from any element, we will get answers in two parts
#           1.) num of subarray inwhich current element is smallest-> number of element in right which are equal or more than current element(find index of next smaller in right)
#           2.) answer calculated till next smaler in right
#           sum both thses scenario at each element, and add to final answer
#           to store answer calculated till NSR , we maintain dp array of size len+1 
class Solution:
    def sumSubarrayMins(self, arr):
        mod=pow(10,9)+7 # as per question requirement
        dp=[0]*(len(arr)+1)
        ans=0
        stack=[]
        for i in range(len(arr)-1,-1,-1):
            while(len(stack) and arr[i]<=arr[stack[-1]]):
                stack.pop()
            
            # if not smaller element in right, then current element will be smallest for all its subarray
            if not len(stack):

                # here (len(arr)-i)) will give num of elements in right inclusive
                ans+=(arr[i]*(len(arr)-i))%mod

                #update dp at every element
                dp[i]=(arr[i]*(len(arr)-i))
            else:
                temp=0

                # here if there is some NSR, then ans will be in two parts

                #1.) ans till NSR-1
                temp+=(arr[i]*(stack[-1]-i))

                #2.) ans from  NSR till end, stored in dp 
                temp+=dp[stack[-1]]


                dp[i]=temp
                ans+=temp%mod
            stack.append(i)
        return ans%mod
                
s=Solution()
arr=[3,1,2,4]
print(s.sumSubarrayMins(arr))