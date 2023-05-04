# task- given a bt , convert it bt that follow rule of child sum i.e sum of child nodes is equal to root
#       operations allowed is we can incremeent node value, not decremenet
# approach - standing at particular node, check left and right node sum, if it is less than curr node, assign any one node value to curr node value
#                                          else assign child sum value to curr
#            then go in left and right, and while comming back sum up left and riht nodes to curr node
# refer striver
def child_sum_property(root):
    child_sum=0
    if root.left: child_sum+=root.left.val
    if root.right: child_sum+=root.right.val

    if child_sum>=root.val:
        root.val=child_sum
    else:
        if root.left: root.left.val=root.val
        elif root.right: root.right.val=root.val
    child_sum_property(root.left)
    child_sum_property(root.right)
    total=0
    if root.left:
        total+=root.left.val
    if root.right:
        total+=root.right.val
    if root.left or root.right:
        root.val=total
    
    # nothting to return because we are doing modification in place , not calculating any result in BT