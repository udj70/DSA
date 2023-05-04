#task- serialize-> convert BT into string, deserialize-> covert string back to bt
# perform LOT 
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.data,end="")
    inorder(root.right)

def serialize(root):
    if not root:
        return ""
    queue=[]
    queue.append(root)
    serialize_st=""
    while(len(queue)):
        node= queue.pop(0)
        
        if node is not None:
            serialize_st+=str(node.data)
            
            queue.append(node.left)
            queue.append(node.right)
            
        else:
            serialize_st+="#"
    print('serialze tree',serialize_st)
    return serialize_st
def deserialize(st):
    if len(st)==0:
        return None
    index=0
    temp=Node(st[index])
    queue=[temp]
    while(len(queue)):

        # for every not null poped node, move index twice to fetch its left and right
        root=queue.pop(0)
        index+=1
        if st[index]!="#":
            root.left=Node(st[index])
            queue.append(root.left)
        #if st[index] have #, i.e there is null to be inserted
        else:
            root.left=None
        index+=1
        if st[index]!="#":
            root.right=Node(st[index])
            queue.append(root.right)
        else:
            root.right=None
    return temp
root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.left.left = Node('E')
root.left.left.right = Node('F')    
root.left.left.right.right = Node('G') 

#print serialize string
serialize_st=serialize(root)

#deserialze string, make tree again
new_root=deserialize(serialize_st)

# print serialized form of tree to check whether tree created is correct
serialize(new_root)