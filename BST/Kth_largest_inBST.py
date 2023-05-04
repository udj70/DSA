global smallest
global count

class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None



def kth_smallest(root,k):
    global count
    global smallest
    if not root:
        return

    #simply perform inorder traversal
    kth_smallest(root.left,k)
    count+=1
    if count==k:
        smallest=root.data
    kth_smallest(root.right,k)


root = Node(11)
root.left = Node(10)
root.right = Node(15)
root.left.left = Node(7)
root.left.left.left = Node(5)
root.left.left.right = Node(8)    
root.left.left.right.right = Node(9) 

smallest=-1
count=0

kth_smallest(root,3)
print(smallest)
