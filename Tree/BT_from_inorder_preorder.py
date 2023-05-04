class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Tree:
    def __init__(self):
        self.root=None  
    def traversal(self):
        self.inorder_traversal(self.root)
    def inorder_traversal(self,root):
        if root==None:
            return
        self.inorder_traversal(root.left)
        print(root.data)
        self.inorder_traversal(root.right)   
        return     

#utility function search
def search(inOrder,data):
    for i in range(len(inOrder)):
        if inOrder[i]==data:
            return i


def create_tree(inOrder,preOrder,inStart,inEnd):
    #no element in inorder
    if inStart>inEnd:
        return None

    tNode=Node(preOrder[create_tree.preindex])  
    create_tree.preindex+=1
    #only one node in inorder
    if inStart==inEnd:
        return tNode  
    #search index tNode.data in inorder
    # and split inorder at that point
    inIndex=search(inOrder,tNode.data)    
    tNode.left=create_tree(inOrder,preOrder,inStart,inIndex-1)
    tNode.right=create_tree(inOrder,preOrder,inIndex+1,inEnd)

    return tNode
create_tree.preindex=0

inOrder = ['D', 'B', 'E', 'A', 'F', 'C']
preOrder = ['A', 'B', 'D', 'E', 'C', 'F']

root=create_tree(inOrder,preOrder,0,len(inOrder)-1)
bt=Tree()
bt.root=root
bt.traversal()