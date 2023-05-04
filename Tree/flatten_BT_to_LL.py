#refer raj vikram aditya
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
global prev
# dry run to better understand
def flatten(root):
    global prev
    if not root:
        return
    # first traverse right and left subtree
    flatten(root.right)
    flatten(root.left)

    # make root.right points to prev
    # root.left to null
    # current root will be new prev
    root.right=prev
    root.left=None
    prev=root


root = Node(11)
root.left = Node(10)
root.right = Node(15)
root.left.left = Node(7)
root.left.left.left = Node(5)
root.left.left.right = Node(8)    
root.left.left.right.right = Node(9) 
prev=None
flatten(root)

while(root):
    print(root.data)
    root=root.right
