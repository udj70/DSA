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

#reverse recursively 
#input-1,2,3,4,5,6,7
#output-7,6,5,4,3,2,1
def reverse_recur(head,prev):
    if head.next==None:
        head.next=prev
        new_head=head

        return new_head
    new_head=reverse_recur(head.next,head)    
    head.next=prev
    return new_head  

# reverse interatively
# input-7,6,5,4,3,2,1
# output-1,2,3,4,5,6,7
def reverse(head):
    prev=None
    curr=head
    while(curr):
        head=curr
        curr=curr.next
        head.next=prev
        prev=head
    return head 



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
new_head=reverse_recur(L.head,None)
L.printLL(new_head)
print()
new_head=reverse(new_head)
L.printLL(new_head)