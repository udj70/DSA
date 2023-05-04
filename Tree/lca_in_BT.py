class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def lca_in_bt(root,data1,data2):
    if root is None:
        return None

    # if one of number match with current root data, return number
    if root.data==data1 or root.data==data2:
        return root.data
    left=lca_in_bt(root.left,data1,data2)
    right=lca_in_bt(root.right,data1,data2)

    # if left return none i.e left not contain desired datas
    if not left:
        return right
    elif not right:
        return left
    else:
    # current node is lca
        return root.data

root = Node(11)
root.left = Node(10)
root.right = Node(15)
root.left.left = Node(7)
root.left.left.left = Node(5)
root.left.left.right = Node(8)    
root.left.left.right.right = Node(9) 
print(lca_in_bt(root,15,9))