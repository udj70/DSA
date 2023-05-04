'''
You are given an integer array arr.

We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.

Return the largest number of chunks we can make to sort the array.
'''

'''
Example 1:

Input: arr = [5,4,3,2,1]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [5, 4], [3, 2, 1] will result in [4, 5, 1, 2, 3], which isn't sorted.
Example 2:

Input: arr = [2,1,3,4,4]
Output: 4
Explanation:
We can split into two chunks, such as [2, 1], [3, 4, 4].
However, splitting into [2, 1], [3], [4], [4] is the highest number of chunks possible.

'''

# approach- make Right min array, store rightmin to current element
#           make l_max variable store left_max to current element
#           if left_max is less than or equal to right minimum of just next element,count+=1
#           dry run , draw graph to better understand

class Solution:
    def maxChunksToSorted(self, arr):
        rmin=[float('inf')]*(len(arr)+1)
        rmin[len(arr)]=float('inf')
        for i in range(len(arr)-1,-1,-1):
            rmin[i]=min(rmin[i+1],arr[i])
        lmax=0
        count=0
        for i in range(len(arr)):
            lmax=max(arr[i],lmax)
            if lmax<=rmin[i+1]:
                count+=1
        return count 
s=Solution()
arr=[1,3,2,5,4,7,6,2]
print(s.maxChunksToSorted(arr)) # [1],[3,2,5,4,7,6,2] 2 partitions
        