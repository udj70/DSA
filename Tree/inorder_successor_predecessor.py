#refer raj vikramaditya channel
global successor
global predessesor
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def inorder_successor(root, element):
    global successor
    if not root:
        return
    # if currenrt root is smaller or equal so it can never be successor, because predessesor is always greater then element
    # so traverse in right tree which have greater elements
    if root.data<=element:
        inorder_successor(root.right, element)
    else:
        # if at any node if node.data is more then element, then it can be potential successor, 
        # but we will search for some bigger node (which is smaller then element) in right tree, if present
        successor=root.data
        inorder_successor(root.left, element)

def inorder_predessesor(root, element):
    global predessesor
    if not root:
        return
    # if cuurent node data is more or equal to element, then predessor will be in left tree

    if root.data>=element:
        inorder_predessesor(root.left, element)
    else:
        # if current node is smaller then element, then it can be predessesor, save it
        # 
        predessesor=root.data
        inorder_predessesor(root.right, element)

root = Node(11)
root.left = Node(10)
root.right = Node(15)
root.left.left = Node(7)
root.left.left.left = Node(5)
root.left.left.right = Node(8)    
root.left.left.right.right = Node(9) 

successor=-1
predessesor=-1

inorder_successor(root, 8)
print("succesor ",successor)

inorder_predessesor(root, 8)
print("predessesor ", predessesor)