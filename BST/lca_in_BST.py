class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def find_lca(root, minElement, maxElement):

    # if current node is itself on of them, then it will be lca itself
    if root.data==minElement or root.data==maxElement:
        return root.data
    
    # if current node follow bst condition with both the min and max element, then cuur node is lca
    if minElement<root.data and maxElement>root.data:
        return root.data
    # if max element is smaller then curr node, i.e both the min and max are smaller , search in left tree
    elif maxElement< root.data:
        return find_lca(root.left, minElement, maxElement)
    else:
    # else min max both are large, search in right tree
        return find_lca(root.right, minElement, maxElement)




root = Node(11)
root.left = Node(10)
root.right = Node(15)
root.left.left = Node(7)
root.left.left.left = Node(5)
root.left.left.right = Node(8)    
root.left.left.right.right = Node(9) 

print(find_lca(root, 8,9 )) # always give first smaller element, then large element