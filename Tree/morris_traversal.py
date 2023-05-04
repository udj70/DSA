#refer raj vikram aditya series
#task- print inoder traversal by morris traversal

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def morris_traversal(root):
    inorder=[]
    curr=root
    while(curr!=None):
        if curr.left is None:
            inorder.append(curr.data)
            curr=curr.right
        else:
            prev=curr.left
            while(prev.right and prev.right!=curr):
                prev=prev.right
            if prev.right is None:
                prev.right=curr
                # inorder.append(curr.data) , add this line in preorder traversal and remove it from else part
                curr=curr.left
            else:
                prev.right = None
                inorder.append(curr.data)
                curr=curr.right
        #print(curr)
    return inorder


root = Node(11)
root.left = Node(10)
root.right = Node(15)
root.left.left = Node(7)
root.left.left.left = Node(5)
root.left.left.right = Node(8)    
root.left.left.right.right = Node(9) 

print(morris_traversal(root))




