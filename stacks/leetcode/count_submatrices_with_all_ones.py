'''
Given an m x n binary matrix mat, return the number of submatrices that have all ones.

Input: mat = [[1,0,1],[1,1,0],[1,1,0]]
Output: 13
Explanation: 
There are 6 rectangles of side 1x1.
There are 2 rectangles of side 1x2.
There are 3 rectangles of side 2x1.
There is 1 rectangle of side 2x2. 
There is 1 rectangle of side 3x1.
Total number of rectangles = 6 + 2 + 3 + 1 + 1 = 13.

'''
# approach- similar as max rectangle with all ones, traverse all rows, 
#           create histogram at each rows, pass histograms height array to helper function
#           helper function-> calculate NSL index, withing that range current heigh can make heights[i]*(i-NSL) submatrices ending at i + answer till NSL
#           at every height calculate submatrices ending at current height, and save it in dp

class Solution:
    def calcSubmatrix(self,arr):
        stack=[-1]
        res=0
        sum_=[0]*len(arr)
        for i in range(len(arr)):
            while(stack[-1]!=-1 and arr[i]<=arr[stack[-1]]):
                stack.pop()
            # if NSL is not their, then range will i+1
            if stack[-1]==-1:
                sum_[i]=arr[i]*(i+1)
            else:
                # if NSl is their then range is i-NSL
                # sum_[i]= submatrices till NSl + submatrices after NSl ending at current index 
                sum_[i]=sum_[stack[-1]]
                sum_[i]+=arr[i]*(i-stack[-1])
            stack.append(i)
        for s in sum_:
            res+=s
        return res
    def numSubmat(self, mat):
        temp=[0]*len(mat[0])
        ans=0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                temp[j]=temp[j]+1 if mat[i][j]==1 else 0
            ans+=self.calcSubmatrix(temp)
        return ans
s=Solution()
mat = [[1,0,1],[1,1,0],[1,1,0]]
print(s.numSubmat(mat))