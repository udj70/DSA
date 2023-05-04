'''Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

It is guaranteed that the answer will in the range of a 32-bit signed integer.'''

# refer strivers series

# approach 1- create a imaginary perfect binary tree(all nodes have two childs, except leaf nodes), index each child,
# in perfect tree left and right childs have index values 2*i +1 and 2*i +2 respectively (0 based indexing, 2*i , 2*i+1 in 1 based indexing)
#  create a hashmap of level-> [left,right] here left and right left min and right max index in a level
# perform preorder traversal and update index of left and right child acc. to above rule
# note- if tree is skew then everytime calculating 2* i will lead to integer overflow(2 x 2 x 2 ....(number of nodes)), so at each level desipite of having real integers , we can index it starting with 0
# to do so, while calculating left child index, 2*(i-1)+1 in place of 2*i +1, similary for riht right child, perform dry run for better understanding
# tc- O(N) sc- O(total levels)




# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution1:
    def solve(self,root,dic,level,index):
        if level in dic:
            dic[level][0]=min(dic[level][0],index)
            dic[level][1]=max(dic[level][1],index)
        else:
            dic[level]=[index,index]
        if root.left:
            self.solve(root.left,dic,level+1,2*(index-1)+1)
        if root.right:
            self.solve(root.right,dic,level+1,2*(index-1)+2)
        
    def widthOfBinaryTree(self, root):
        dic={}
        mx=0
        self.solve(root,dic,0,1)
        #print(dic)
        for k in dic.keys():
            mx=max(mx,dic[k][1]-dic[k][0]+1)
        return mx


s=Solution1()

root=TreeNode(2)
root.left=TreeNode(4)
root.left.left=TreeNode(6)
root.right=TreeNode(7)
root.right.right=TreeNode(9)

print(s.widthOfBinaryTree(root)) # max width will have nodes (6 ,null ,null ,9)


# approach 2
# as we are dealing with level so can perform level order traversal and store tuple of (node, index) in queue
# at each level traverse all nodes and store left and right , calc difference

#tc - O(N) sc= O(N)
def calc_width(root):
    queue=[]
    mx=0
    queue.append([root,1])
    while(len(queue)):
        
        size=len(queue)
        # indexes of first and last element in level
        first=0
        last=0
        for i in range(size):
            node=queue.pop(0)
            curr_node=node[0]
            curr_index=node[1]
            if i==0:
                first=curr_index
            if i==size-1:
                last=curr_index

            # to avoid integer overflow, update curr index to currindex-1, so that every level wil have index starting from 0
            updated_index=curr_index-1
            
            if curr_node.left:
                queue.append([curr_node.left,2*updated_index+1])
            if curr_node.right:
                queue.append([curr_node.right,2*updated_index+2])
            
            mx=max(mx,last-first+1)
    return mx

print(calc_width(root))