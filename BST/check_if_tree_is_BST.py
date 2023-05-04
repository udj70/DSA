class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class ReturnNode:
    def __init__(self,maxElement,minElement,size):
        self.maxElement=maxElement
        self.minElement=minElement
        self.size=size
def check_if_BST(root):
    if not root:
        # if root is None set maxElement INT_MIN and minElement as INT_MAX, so that its parent will be BST
        return ReturnNode(float('-inf'),float('inf'),0)

    left=check_if_BST(root.left)
    right=check_if_BST(root.right)

    # if root data is more that left subtree max and less then right subtree min, the it is BST, increment size
    #   maxElement will be max of root and right max, and minElement will be min of root and leftmin
    if root.data>left.maxElement and root.data<right.minElement:
        return ReturnNode(max(root.data,right.maxElement), min(root.data,left.minElement), left.size+right.size+1)
    # if current is not BST then set maxElemtn and min Element to extreme max and min, so that above subtree will never pass BST if condition
    # and set return size to 0
    return ReturnNode(float('inf'),float('-inf'),0)



root = Node(11)
root.left = Node(10)
root.right = Node(15)
root.left.left = Node(7)
root.left.left.left = Node(5)
root.left.left.right = Node(8)    
root.left.left.right.right = Node(9) 
if check_if_BST(root).size:
    print("It is BST")
else:
    print("Not BST")