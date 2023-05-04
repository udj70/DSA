# refer raj vikram aditya series
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

def BST_from_preorder(preorder,bound):
    #if preorder arrya is finished or current element in preorder is less more that upper bound, then it can't be inserted, insert none
    if BST_from_preorder.preindex==len(preorder) or preorder[BST_from_preorder.preindex]>bound:
        return None
    

    root=Node(preorder[BST_from_preorder.preindex])
    BST_from_preorder.preindex+=1

    # pass upper bound , to check whether next element can be inserted
    # for left tree upper bound will be current root data
    root.left= BST_from_preorder(preorder, root.data)
    # for right subtree upper bound will be previous bound itself
    root.right = BST_from_preorder(preorder,  bound)

    return root






preorder=[11,7,5,8,13,12,14]
BST_from_preorder.preindex=0
root= BST_from_preorder(preorder,float('inf'))


inorder(root)



# approach 2- using monotonic stack- push first node initially in stack which is root,
#             move ahead in preorder array, and those elements are smaller will simply become left of stack.top(), adn push them in stack
#             if we got bigger element, then remove all smaller from stack, last removed element right will be current element, push last removed right now in stack

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class Solution:
   
    def bstFromPreorder(self, preorder):
            root=TreeNode(preorder[0])  
            stack=[root]
            for val in preorder[1:]:
                if val<stack[-1].data:
                    stack[-1].left=TreeNode(val)
                    stack.append(stack[-1].left)
                else:
                    while(len(stack) and stack[-1].data<val):
                        last=stack.pop()
                    last.right=TreeNode(val)
                    stack.append(last.right)
            return root
preorder=[11,7,5,8,13,12,14]
s=Solution()
root=s.bstFromPreorder(preorder)
print()
inorder(root)