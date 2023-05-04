# task- Given a BST, inwhich two nodes are swapped, find them and coorect them
# approach 1- save inorder traversal in array, sort it, again do inorder traversal in tree, correct data using array data
#           TC- O(NlogN + O(N)) SC- O(N)
# 
# approach 2- perform single inorder traversal, check at every node where condition broke i.e. curr,data<prev.data
#               save prev in first, curr in middle, and then search second break point, where curr.data<prev.data
#               save curr in last
#              now there will be 2 scenarios-1. if adjacenent nodes are swapped, i.e first and middle one are swapped
#                                           2. if non adjacent swapped i.e first and last swapped
global first
global middle
global last
global prev
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def traversal(root):
    if not root:
        return
    traversal(root.left)
    print(root.data, end=" ")
    traversal(root.right)
def inorder(root):
    global first
    global middle
    global last
    global prev
    if not root:
        return None
    inorder(root.left)
    # if prev is none. i.e we are at first element of inorder
    # if root.data<prev.data condition occurs, i.e curr and prev are not in proper place, save them for future reference
    if prev is not None and root.data<prev.data:
        # if first is null, i.e. this is first occurence of faulty condition, prev and curr
        if not first:
            first=prev
            middle=root
        # i.e this second occurence, so only save curr node
        else:
            last=root
    else:
        prev=root
    inorder(root.right)

def correct_BST(root):
    inorder(root)
    #print(first.data,middle.data)

    # if last is none, that is it is first condition, adjacent nodes are swapped
    if last is None:
        first.data,middle.data= middle.data, first.data
    # ignore middle, only swap first and last
    else:
        first.data,last.data = last.data, first.data
    
root = Node(11)
root.left = Node(10)
root.right = Node(15)
root.left.left = Node(5)
root.left.left.left = Node(7)
root.left.left.right = Node(8)    
root.left.left.right.right = Node(9) 
#traversal(root)
first=None
middle=None
last=None
prev=None
correct_BST(root)
traversal(root)