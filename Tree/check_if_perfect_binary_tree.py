# perfect Bt- whose all leafs at last level
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def check_if_perfect_bt(root):
    #perform LOT and check relation between count of node at each level, and level number i.e 2^(l-1) == counts of nodes
    level=1
    count=0
    queue = [root,None]
    flag=False
    while(len(queue)):
        node = queue.pop(0)
            
        if node == None:
            if pow(2,level-1) != count:
                flag=True
                break
            elif len(queue):
                queue.append(None)
                level+=1
                count=0
                
        
        else:
            count+=1
            if node.left :
                queue.append(node.left)
            if node.right :
                queue.append(node.right)
           
    if not flag:
        print("is perfect BT")
    else:
        print("not perfect BT")


root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
#root.right.right=Node(7)
check_if_perfect_bt(root)