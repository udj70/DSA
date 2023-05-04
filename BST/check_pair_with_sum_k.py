# same as BST iterator approach, just add before() function to traverse from last
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BST:
    def __init__(self,root):
        self.root=root
        self.left_stack=[]
        self.right_stack=[]
        self.pushAllleftStack(root)
        self.pushAllrightStack(root)
    def pushAllleftStack(self,root):
        while(root):
            self.left_stack.append(root)
            root=root.left
    def pushAllrightStack(self,root):
        while(root):
            self.right_stack.append(root)
            root=root.right
    def next(self):
        node=self.left_stack.pop()
        if node.right:
            self.pushAllleftStack(node.right)
        return node.data
    def before(self):
        node=self.right_stack.pop()
        if node.left:
            self.pushAllrightStack(node.left)
        return node.data
    




root = Node(11)
root.left = Node(10)
root.right = Node(15)
root.left.left = Node(7)
root.left.left.left = Node(5)
root.left.left.right = Node(8)    
root.left.left.right.right = Node(9) 
bst=BST(root)

s=12
i=bst.next()
j=bst.before()

while(i<=j):
    
    if i+j==s:
        print(i,j) # 5,7
        break
    elif i+j<s:
        i=bst.next()
    else:
        j=bst.before()

