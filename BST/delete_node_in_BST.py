#refer strivers video for referrence
class Node:
    def __init__(self,data):
        self.info=data
        self.left=None
        self.right=None

def traversal(root):
    if not root:
        return
    traversal(root.left)
    print(root.info, end=" ")
    traversal(root.right)


def last_right(root):
    if not root.right:
        return root
    return last_right(root.right)    

def helper(root):
    #if root left is none then return root right subtree
    if not root.left:
        return root.right

    if not root.right:
        return root.left

    #now pick largest in left subtree and assign its right to cuurent root right    
    right_child=root.right
    #get largest node in left subtree
   
    last_right_in_left=last_right(root.left)
    #and assign its right to current root right
    last_right_in_left.right=right_child
    return root.left      

def delete_node(root,key):
    #if root is not there then no node deletion
    if not root:
        return None
    #cuurent root is key, then call helper function on it    
    if root.info==key:
        return helper(root)
    dummy=root        #save root in dummy
    while(root):
        if root.info>key:#go in left subtree
            #if key is root left, assign cuurent root left node return by helper
            if root.left and root.left.info==key:
                root.left=helper(root.left)
            else:
                #else just traverse in left
                root=root.left
        else:
            # if key is root right, assign current root right to node returned by helper
            if root.right and root.right.info==key:
                root.right=helper(root.right)
            else:
                root=root.right
    return dummy #return dummy node, as it is original parent


root = Node(11)
root.left = Node(10)
root.right = Node(15)
root.left.left = Node(7)
root.left.left.left = Node(5)
root.left.left.right = Node(8)    
root.left.left.right.right = Node(9) 

new_root=delete_node(root,7)
traversal(new_root)