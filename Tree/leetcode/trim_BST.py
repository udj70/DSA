'''Given the root of a binary search tree and the lowest and highest boundaries as low and high, trim the tree so that all its elements lies in [low, high]. Trimming the tree should not change the relative structure of the elements that will remain in the tree (i.e., any node's descendant should remain a descendant). It can be proven that there is a unique answer.

Return the root of the trimmed binary search tree. Note that the root may change depending on the given bounds.'''

# approach - if root.val is more than high, then go in left subtree and return new root
#           if root.val is less than low, then go in right subtree and return new root
#           if root is correct then got in left and right subree both , return node will be left and right of current node

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def traversal(self,root):
        if not root:
            return
        self.traversal(root.left)
        print(root.val,end="")
        self.traversal(root.right)

    def trimBST(self, root, low, high) :
        if not root:
            return None
        if root.val>high:
            return self.trimBST(root.left,low,high) if root.left else None
        if root.val<low:
            return self.trimBST(root.right,low,high) if root.right else None
        root.left=self.trimBST(root.left,low,high)
        root.right=self.trimBST(root.right,low,high)
        return root
s=Solution()
root=TreeNode(3)
root.left=TreeNode(1)
root.left.right=TreeNode(2)
root.right=TreeNode(5)
root.right.left=TreeNode(4)
low=2
high=4
s.traversal(s.trimBST(root,low,high))