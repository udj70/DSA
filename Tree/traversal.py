import insert
import sys
sys.path.append('H:\Python\Queue_LL')
import createQueue

def inorder(r):
    if r:    
        inorder(r.left)
        print(r.data)
        inorder(r.right)

def postorder(r):
    if r:
        postorder(r.left)
        postorder(r.right)
        print(r.data)
def preorder(r):
    if r:
        print(r.data)
        preorder(r.left)
        preorder(r.right)
def level_order(r):
     q=createQueue.Queue()
     if not r:
         return 
     else:
         q.Enqueue(r)
         while(not q.IsEmptyQueue()):
             temp=q.Dequeue()
             if temp.left:
                 q.Enqueue(temp.left)
             if temp.right:
                 q.Enqueue(temp.right)
             print(temp.data)            

  #  temp=r
   # while(not q.Isempty()):

#preorder non recursive
def preorder_nr(root):
    stack=[]
    if not root:
        return
    while(1):
        while(root):
            #acess the root
            print(root.data)
            stack.append(root)
            root=root.left
        if not len(stack):
            break
        root=stack.pop()
        #indicate completion of left subtree and current node,now go to right subtree
        root=root.right

#inorder non recursive
def inorder_nr(root):
    stack=[]
    if not root:
        return
    while(True):
        while(root):
            stack.append(root)
            root=root.left
        if not len(stack):
            break
        root=stack.pop()
        print(root.data)
        root=root.right  

#postorder non recursive
def postorder_nr(r):

    if not r:
        return
    stack=[]
    stack.append(r)
    prev=None
    while(len(stack)):
        current=stack[-1]
        if  prev==None or prev.left==current or prev.right==current:
            if current.left:
                stack.append(current.left)
            elif current.right:
                stack.append(current.right)
        elif current.left==prev:
            if current.right:
                stack.append(current.right)
        else:
            print(current.data)
            stack.pop()
        prev=current


#zigzag traversal
def zigzag(root):
    even=[]
    odd=[]
    l=0
    even.append(root)
    while(len(even) or len(odd)):
        if l%2==0:
            if not len(even):
                l+=1
                continue
            q=even.pop()
            print(q.data)
            if q.left:
                odd.append(q.left)
            if q.right:
                odd.append(q.right)
        else:
            if not len(odd):
                l+=1
                continue
            q=odd.pop()
            print(q.data)
            if q.right:
                even.append(q.right)
            if q.left:
                even.append(q.left)
def leftView(root):
    queue=[]
    queue.append(root)
    queue.append(None)
    flag=True
    while(len(queue)):
        q=queue.pop(0)
        if q==None and len(queue):
            queue.append(None)
            flag=True
        elif len(queue):
            if flag:
                flag=False
                print(q.data)
            if q.left:
                queue.append(q.left)
            if q.right:
                queue.append(q.right)
        else:
            break            
def rightView(root):
    queue=[]
    queue.append(root)
    queue.append(None)
    flag=True
    while(len(queue)):
        q=queue.pop(0)
        if q==None and len(queue):
            queue.append(None)
            flag=True
        elif len(queue):
            if flag:
                flag=False
                print(q.data)
            if q.right:
                queue.append(q.right)    
    
            if q.left:
                queue.append(q.left)
        else:
            break           


           






                


r=insert.insert(1,2,3,4,5,6,7)
print("inorder of tree:")
inorder(r)
print("inorder non recursive:")
inorder_nr(r)
print("postorder of tree:")
postorder(r)
print("postorder non recursive")
postorder_nr(r)
print("preorder of tree:")
preorder(r)
print("preorder non recursive:")
preorder_nr(r)
print("level order of tree")
level_order(r)
print("zigzag traversal")
zigzag(r)
print("left view")
leftView(r)
print("rightView")
rightView(r)


