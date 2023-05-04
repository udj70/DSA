from numpy import cumsum
from requests import head


class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.last=None
    def insert(self,data):
        new_node=node(data)
        if not self.head:
            self.head=new_node
            self.last=new_node
        else:
            self.last.next=new_node
            self.last=new_node
    def printLL(self,head):
        temp=head 
        while(temp):
            print(temp.data,end=" ") 
            temp=temp.next            

#SC-O(k)
#TC-O(n) 
def reverseLLingroupUsingStack(head,k):
    curr=head
    prev=None
    count=0
    stack=[]
    while(curr):
        count=0
        while curr and count<k:
            stack.append(curr)
            curr=curr.next
            count+=1
        while(len(stack)):
            if prev is None:
                prev=stack.pop()
                head=prev
            else:
                prev.next=stack.pop()
                prev=prev.next
    prev.next=None
    return head                    


#TC-o(n)
#SC-o(1)
def reverseLLingroup(head,k):
    curr=head
    prev=None
    next=None
    count=0
    while(curr and count<k):
        next=curr.next
        curr.next=prev
        prev=curr
        curr=next
        count+=1
    if next:    
        head.next=reverseLLingroup(next,k)
    return prev        




L=LinkedList()
L.insert(1)
L.insert(2)
L.insert(3)
L.insert(4)
L.insert(5)
L.insert(6)
L.insert(7)  
L.printLL(L.head)
print()
new_head=reverseLLingroup(L.head,2)
L.printLL(new_head)  
print()
new_head=reverseLLingroupUsingStack(new_head,2)
L.printLL(new_head)



