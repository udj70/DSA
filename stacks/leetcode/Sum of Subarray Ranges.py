'''
You are given an integer array nums. The range of a subarray of nums is the difference between the largest and smallest element in the subarray.

Return the sum of all subarray ranges of nums.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,2,3]
Output: 4
Explanation: The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0 
[2], range = 2 - 2 = 0
[3], range = 3 - 3 = 0
[1,2], range = 2 - 1 = 1
[2,3], range = 3 - 2 = 1
[1,2,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.

'''

# approach 1- using two loops make all possible subbarays and calculate their max and min difference at the same time
#             tc- O(n^2)
# approach 2- for instance there are n subbarays, so answer= (l1-m1)+(l2-m2).....Ln-Mn (here l and m are largest and smallest in each subbaray)
#             answer= (l1+l2+l3.....Ln)-(m1+m2+m3....Mn)
#             In short calculate all smallest in subaarays and all largest in subarrays
#              to do so, on each array element we can calculate for how manay element in left and right current element can act as  smallest i.e find next smaller in left, and next smaller in right index
#              similary for all largest in subarray, calculate NGL and NGR
#              similar approach as max size rectangle in histogram
#              number of sub arrays formed by current eleemnt as min/max= num of element smaller/larger in left * num of elements smaller/larger in right* A[current]

# note- in bellow solution we have calculted left and right smalelr in single pass while popping, dry run tu visualize better

class Solution:
    def subArrayRanges(self, nums):
        ans=0
        # sum of larger in subarrays
        inf=float('inf')

        # modified array, added inf at both ends to get left and right extreme out of bound index i.e -1 and len(arr)
        # -inf because we are calculating NSL,NSR and will use inf while calculating NGL,NGR
        A1=[-inf]+nums[:]+[-inf]
        stack=[]
        for i in range(len(A1)):
            while(stack and A1[i]<A1[stack[-1]]):
                # element which is popped is smaller all elemments less than i, and more then stack.top()
                m=stack.pop()
                n=stack[-1]

                # so A[m] is smaller for left range m-n and right range i-m

                # because popped eleemnt is smaller we will subtract its contribution from final answer
                ans-=A1[m]*(m-n)*(i-m)
            stack.append(i)
           
        A1=[inf]+nums[:]+[inf]
        stack=[]
        for i in range(len(A1)):
            while(stack and A1[i]>A1[stack[-1]]):
                m=stack.pop()
                n=stack[-1]
                ans+=A1[m]*(m-n)*(i-m)
            stack.append(i)
            
        return ans

nums = [1,2,3]
s=Solution()

print(s.subArrayRanges(nums)) # 4