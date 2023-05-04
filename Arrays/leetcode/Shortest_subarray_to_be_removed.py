'''
Given an integer array arr, remove a subarray (can be empty) from arr such that the remaining elements in arr are non-decreasing.

Return the length of the shortest subarray to remove.

A subarray is a contiguous subsequence of the array.

 

Example 1:

Input: arr = [1,2,3,10,4,2,3,5]
Output: 3
Explanation: The shortest subarray we can remove is [10,4,2] of length 3. The remaining elements after that will be [1,2,3,3,5] which are sorted.
Another correct solution is to remove the subarray [3,10,4].

'''
#approach- 2 pointer- subarray to be removed will be either form middle, or left or right,
#          check increasing range from start, end using two pointers,
#          if increasing range from start is till last of array, then no element to be removed.
#          similarly check increasing range from last
#          if we have to pick increasing range from start or last will we consider smallest removed subarray
#          else: subarray to be removed will be in middle, run while loop

class Solution:
    def findLengthOfShortestSubarray(self, arr):
        s=0
        e=len(arr)-1
        while(s<len(arr)-1 and arr[s]<=arr[s+1]):
            s+=1
        if s==len(arr)-1:
            return 0
        while(e>=s and arr[e]>=arr[e-1] ):
            e-=1
        if e==0:
            return len(arr)-1
    
        result=min(len(arr)-1-s,e)
        i=0
        j=e
        while(i<=s and j<len(arr)):
            if arr[i]<=arr[j]:
                result=min(result,j-i-1)
                i+=1
            else:
                j+=1
        return result