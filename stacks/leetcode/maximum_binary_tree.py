'''
You are given an integer array nums with no duplicates. A maximum binary tree can be built recursively from nums using the following algorithm:

Create a root node whose value is the maximum value in nums.
Recursively build the left subtree on the subarray prefix to the left of the maximum value.
Recursively build the right subtree on the subarray suffix to the right of the maximum value.
Return the maximum binary tree built from nums.

'''
# refer leetcode for examples

# approach 1- get max in array, and build tree from left and right portion
#           tc- O(n^2) 

# approach 2- usings monotonic stack, traverse array, create Node , then all those elements which are popped by current element will be childs of current element,
#             popped elemens will be in ascending order, so first poped will be last in subtree, assign its right to null, update right child variable to current node
#             after popping, if nothing poped so assing left child of current node to null
#                             else, left child will be last popped element stored in right child variable
#           at the end, remaing stack element are popped and inserted in tree, in right of stack[0]
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class Solution:
    def constructMaximumBinaryTree(self, nums):
        stack = []
        
        for num in nums:
            new_node = TreeNode(num)
            
            right_child = None
            while stack and stack[-1].val < num:
                node = stack.pop()
                node.right = right_child
                right_child = node
            
            # if some elemtn popped then they will come under left child, else left child will be None
            new_node.left = right_child
            stack.append(new_node)
        
        root = None
        while stack:
            node = stack.pop()
            node.right = root
            root = node
        
        return root 
s=Solution()
arr=[3,2,1,6,0,5]
root=s.constructMaximumBinaryTree(arr)