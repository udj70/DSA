#task- Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

#       The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).
# refer leetcode for more detail
# approach 1- go at every node by dfs and then for each node genarate all possible path sum in left an right subtree, and increase count if same as target
# approach 2- looks like finding sub array sum in tree in while going down wards, so to find subarray sum we maintain prefix sum ie. sum of node till current node,
# and will check in hash map currsum- target , if present will add its count in answer, and add cuurSum in hash map
# while returning back from curr node, reduce cuurSum count by one, because currSum will no longer be important for other branches

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
global ans
class Solution:
    def solve(self,root,target,currSum,dic):
        global ans
        if not root:
            return 0

        # same logic as prefix sum to calculate subarray sum in linear array
        currSum+=root.val
        if currSum-target in dic:
            ans+=dic[currSum-target]
        if currSum in dic:
            dic[currSum]+=1
        else:
            dic[currSum]=1
        
        
        self.solve(root.left,target,currSum,dic)
        self.solve(root.right,target,currSum,dic)
        
        dic[currSum]-=1
        
            
    def pathSum(self, root, targetSum):
        global ans
        ans=0
        dic={0:1}
        self.solve(root,targetSum,0,dic)
        return ans
s=Solution()
root=TreeNode(5)
root.left=TreeNode(-1)
root.right=TreeNode(4)
print(s.pathSum(root,4)) # 2-> 5+-1 and 4