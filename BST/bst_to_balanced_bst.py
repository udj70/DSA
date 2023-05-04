class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def array_to_BBST(arr,start,end):
    #got sorted array
    #divide into half
    #and assign left part to left and right part to right subtree respectively
    if start>end:
        return None
    mid=(start+end)//2
    root=Node(arr[mid])
    root.left=array_to_BBST(arr,start,mid-1)
    root.right=array_to_BBST(arr,mid+1,end)


    return root
def get_inorderUtil(arr,root):
    if not root:
        return
    get_inorderUtil(arr,root.left)
    arr.append(root.data)
    get_inorderUtil(arr,root.right)


def get_BBST(root):
    arr=[]
    get_inorderUtil(arr,root)    
    return array_to_BBST(arr,0,len(arr)-1)

root = Node(10)
root.left = Node(8)
root.left.left = Node(7)
root.left.left.left = Node(6)
root.left.left.left.left = Node(5)    
new_root=get_BBST(root)