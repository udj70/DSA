class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None
    
    #create of tree by passing node value  as parameter
    def create(self, val):  #binary search is create here

        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break
ans=0
def diameterTree(root,temp):
    global ans
    if not root:
        return 0
    left=diameterTree(root.left,temp)
    right=diameterTree(root.right,temp)
    temp=max(left,right)+1
    ans=max(ans,left+right+1)
    
    return temp 

       
tree=BinarySearchTree()
t = int(input()) #number of elements in tree

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])
print(diameterTree(tree.root,0))    