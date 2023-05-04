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
    def create(self, val):  
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

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
#when hd is not data member of tree data structue
def bottomView(root):
    q=[]
    hd=0 #horizontal distance
    new_dic={}
    q.append([root,hd])
    #print(q[0][1],q[0][0].info)
    while(len(q)):
        temp=q[0]
        
        #only differnece between the bottom view and top view is first node corresponding 
        #to a horizontal distance is considered in case of top view and last node in case of bottom view
        new_dic[temp[1]]=temp[0].info    
        
        
        if temp[0].left:
            #new_dic[temp[1]-1]=temp[0].left.info
            q.append([temp[0].left,temp[1]-1])
        if temp[0].right:
            #new_dic[temp[1]+1]=temp[0].right.info
            q.append([temp[0].right,temp[1]+1])
            
        q.pop(0)    
    for v in sorted(new_dic):
        print(new_dic[v],end=' ')    


#when hd is data member of tree data structure
'''def topview(root) : 
  
    if(root == None) : 
        return
    q = [] 
    m = dict() 
    hd = 0
    root.hd = hd  
  
    # push node and horizontal 
    # distance to queue  
    q.append(root)  
  
    while(len(q)) : 
        root = q[0] 
        hd = root.hd  
          
        # count function returns 1 if the  
        # container contains an element  
        # whose key is equivalent to hd,  
        # or returns zero otherwise.  
        
        m[hd] = root.data  
        if(root.left) :          
            root.left.hd = hd - 1
            q.append(root.left)  
          
        if(root.right):          
            root.right.hd = hd + 1
            q.append(root.right)  
          
        q.pop(0) 
    for i in sorted (m): 
        print(m[i], end = "")  
   '''       
        
                 



    
   



tree = BinarySearchTree()
t = int(input()) #number of elements in tree

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])
print('bottom view:')
bottomView(tree.root)