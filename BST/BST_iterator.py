#naive approach- store inoder in array and perform operations
# TC- O(N), SC-O(N)

#TC- O(H) SC- O(H)
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BST:
    def __init__(self,root):
        self.root=root
        self.stack=[]
        self.pushAll(root)
    # whenever we reach at any node, we push its left left childs in stack before accessing current node.(inorder means- left->node->right)
    def pushAll(self,root):
        while(root):
            self.stack.append(root)
            root=root.left
    # if stack have some element to access , so it have next value, else not
    def hasNext(self):
        if len(self.stack):
            return True
        return False
    # pop top of stack, it is current next print it, push all its right childs using pushAll mechanism
    def next(self):
        if len(self.stack):
            node=self.stack.pop()
            self.pushAll(node.right)
            return node.data
        # if len of stack is 0, then no next element
        return None
root = Node(11)
root.left = Node(10)
root.right = Node(15)
root.left.left = Node(7)
root.left.left.left = Node(5)
root.left.left.right = Node(8)    
root.left.left.right.right = Node(9) 
bst=BST(root)
print(bst.next())
print(bst.hasNext())
print(bst.next())