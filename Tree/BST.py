class node:
    def __init__(self,data=None):
        self.data=data
        self.left=None
        self.right=None
class BST:
    def __init__(self):
        self.root=None
    def insert(self,data):
        newnode=node(data)
        if not self.root:
            self.root=newnode
        else:
            current=self.root
            while(True):
                if data<current.data:
                    if not current.left:
                        current.left=newnode
                        break
                    else:
                        current=current.left
                if data>current.data:
                    if not current.right:
                        current.right=newnode
                        break
                    else:
                        current=current.right

    def inorder_r(self,r):
        if not r:
            return
        self.inorder_r(r.left)
        print(r.data)
        self.inorder_r(r.right)
        return
    def inorder_nr(self,r):
        stack=[]
        if not r:
            return

        while(True):
            while(r):
                stack.append(r)
                r=r.left
            if not len(stack):
                   break
            r=stack.pop()
            print(r.data)
            r=r.right
    def preorder_r(self,r):
        if not r:
            return
        print(r.data)
        self.preorder_r(r.left)
        self.preorder_r(r.right)
    def preorder_nr(self,r):
        stack=[]
        if not r:
            return
        while(True):
            while(r):
                print(r.data)
                stack.append(r)
                r=r.left
            if not len(stack):
                break

            r=stack.pop()
            r=r.right
    def postorder_r(self,r):
        if not r:
            return
        self.postorder_r(r.left)
        self.postorder_r(r.right)
        print(r.data)
    def postorder_nr(self,r):
        stack=[]
        stack.append(r)
        prev=None
        while(len(stack)):
            curr=stack[-1] 
            if prev==None or prev.left==curr or prev.right==curr:
                if curr.left:
                    stack.append(curr.left)
                elif curr.right:
                    stack.append(curr.right)
            elif prev==curr.left:
                if curr.right:
                    stack.append(curr.right)
            else:
                print(curr.data)
                stack.pop()
            prev=curr
    def LCA(self,r,a,b):
        if not r:
            return
        while(True):    
            if (a<r.data and b>r.data) or (b<r.data and a>r.data):
                return r.data
            if r.data==a or r.data==b:
                return r.data    
            if a<r.data and r.left:
                    r=r.left
            elif r.right:    
                    r=r.right

                 
b=BST()
arr=[3,2,5,6,1,7,8]
for a in arr:
    b.insert(a)
b.inorder_r(b.root)      
print()          
b.inorder_nr(b.root)
print()
b.preorder_r(b.root)
print()
b.preorder_nr(b.root)
print("postorder recursive")
b.postorder_r(b.root)
print("postorder non recursive")
b.postorder_nr(b.root)
print("LCA of two nodes")
print(b.LCA(b.root,6,7))


