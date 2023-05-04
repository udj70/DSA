'''We run a preorder depth-first search (DFS) on the root of a binary tree.

At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  If the depth of a node is D, the depth of its immediate child is D + 1.  The depth of the root node is 0.

If a node has only one child, that child is guaranteed to be the left child.

Given the output traversal of this traversal, recover the tree and return its root.

ex-
Input: traversal = "1-2--3--4-5--6--7"
Output: [1,2,5,3,4,6,7]
'''

# Definition for a binary tree node.

# approach- 
# Intuition- If prev count of dash is 1 less than current dashes then current number is child of prev number, else return None
# Maintain a global preindex to traverse string
# Intial count of dash is -1
# At every function call calculate number  of dahses starting from preindex till next number in string
# if number of dashes is one more than the prev_dash i.e current number is child of previous 

# so fetch current number, create TreeNode
# update preindex to just next index after current number
# make recursive calls with current_dashes_count+1 to get left and right child
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
global preindex
class Solution:
    def solve(self,prev_dash,traversal):
        global preindex

        # if traversal string is completed
        if preindex==len(traversal):
            return None

        # store preindex in temp and traverse temp
        tempindex=preindex
        count=0

        # get current dashes count
        while(traversal[tempindex]=='-'):
            tempindex+=1
            count+=1
        
        # current_dash ! = prev+1 i.e current number is not child of prev
        if prev_dash+1 != count:
            return None
        
        # fetch current number , get its start and end index 
        start=tempindex
        while(tempindex<len(traversal) and traversal[tempindex]!='-'):
            tempindex+=1
        end=tempindex

        # extract number from string and make treeNode
        root=TreeNode(traversal[start:end])

        # update preindex
        preindex=tempindex

        # calculate left and right child
        root.left=self.solve(count,traversal)
        root.right=self.solve(count,traversal)
        return root
        
    def recoverFromPreorder(self, traversal):
        global preindex
        preindex=0

        # current dash count is -1
        return self.solve(-1,traversal)