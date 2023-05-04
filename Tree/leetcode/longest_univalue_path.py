'''
Given the root of a binary tree, return the length of the longest path, where each node in the path has the same value. This path may or may not pass through the root.

The length of the path between two nodes is represented by the number of edges between them.'''


#approach- standing at any node make a call on left and right subtree,
#           it will return max univalue path from left and right
#           now there are two situations- 1. max univalue path pass from current node
#                                            - check if left ,current and right node is same, so update ans with max(ans , left+right+1)
#                                         2. max univalue path not pass from current node, so return max from left or right
#                                            - if only left val is same as current val, left_ans=left+1
#                                               or 
#                                            - if only right val is same as current val, right_ans=right+1
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
global ans
class Solution:
    def solve(self,root):
        global ans
        if not root:
            return 0
        left=self.solve(root.left)
        right=self.solve(root.right)
        if left and right:
            if root.val==root.left.val and root.val==root.right.val:
                ans=max(ans,left+right+1)
                return max(left,right)+1
        left_ans=1
        right_ans=1
        if left:
            if root.val==root.left.val:
                left_ans=left+1
                ans=max(ans,left+1)
           
        if right:
            if root.val==root.right.val:
                right_ans=right+1
                ans=max(ans,right+1)
        ans=max(ans,left_ans,right_ans)
        return max(left_ans,right_ans)
    
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        global ans
        ans=0
        self.solve(root)
        return ans-1