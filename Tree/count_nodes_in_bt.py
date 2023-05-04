# task- given complete BT , i.e all levels are completely filled  despite lowest level 
#       count nodes in it
# approach 1- inorder traversal, TC- O(n)
# approach 2- at every node, if below subtree have all filled nodes, so nodes in that subtree will be 2^h-1
#                            else go in left and right subtree and 1 to answer and return

# tc= O((logn)^2),refer striver
def calc_left_height(root):
    height=0
    while(root):
        height+=1
        root=root.left
    return height
def calc_right_height(root):
    height=0
    while(root):
        height+=1
        root=root.right
    return height
def count_node_in_bt(root):
    if not root:
        return 0
    # if left and right of current subree is same , i.e it have all level filled node at each level
    
    left_height=calc_left_height(root.left)
    right_height=calc_right_height(root.right)

    if left_height == right_height:
        # calculate 2^height - 1
        return (1<<left_height)-1
    return 1+count_node_in_bt(root.left)+count_node_in_bt(root.right)

