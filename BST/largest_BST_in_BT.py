class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def largest_BST_util(root):
    if not root:
        return [0,True,0,float('inf')] #[largest_size,bool,maxElement,minElement]  

    left=largest_BST_util(root.left)
    right=largest_BST_util(root.right)
    bool=False
    #intially set largest size to max value returned by left or right
    largest_size=max(left[0],right[0])
    maxElement=max(left[2],right[2],root.data)
    minElement=min(left[3],right[3],root.data)
    #if left and right both subtree are bst only check of current node
    if left[1] and right[1]:
        #if left and right are subtree then check bst condition of current node
        if left[2]<root.data and right[3]>root.data:
            bool=True
            #update largest size
            largest_size=1+left[0]+right[0]
    return [largest_size,bool,maxElement,minElement]            

def largest_BST(root):
    largest_size,bool,maxElement,minElement=largest_BST_util(root)
    return largest_size




''''BEST CODE'''


#code by raj vikramaditya lectures
# total same as check_if_BST, only diff is if at node BST cannot be formed so return value of size will max(left.size, right.size)
class ReturnNode:
    def __init__(self,maxElement,minElement,size):
        self.maxElement=maxElement
        self.minElement=minElement
        self.size=size
def largestBSTCleanCode(root):
    if not root:
        # if root is None set maxElement INT_MIN and minElement as INT_MAX, so that its parent will be BST
        return ReturnNode(float('-inf'),float('inf'),0)

    left=largestBSTCleanCode(root.left)
    right=largestBSTCleanCode(root.right)

    # if root data is more that left subtree max and less then right subtree min, the it is BST, increment size
    #   maxElement will be max of root and right max, and minElement will be min of root and leftmin
    if root.data>left.maxElement and root.data<right.minElement:
        return ReturnNode(max(root.data,right.maxElement), min(root.data,left.minElement), left.size+right.size+1)
    # if current is not BST then set maxElemtn and min Element to extreme max and min, so that above subtree will never pass BST if condition
    # and set size max(left.size, right.size) 
    return ReturnNode(float('inf'),float('-inf'),max(left.size,right.size))




root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(7)
root.left.left.left = Node(5)
root.left.left.right = Node(8)    
root.left.left.right.right = Node(9) 
size=largest_BST(root)        
print(size) #4

print(largestBSTCleanCode(root).size) #4