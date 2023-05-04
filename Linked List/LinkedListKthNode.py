class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def insert(self,data):
        newnode=node(data)
        if self.head==None:
            self.head=newnode
        else:
            temp=self.head
            while(temp.next):
                temp=temp.next
            temp.next=newnode
    def RootNthNode(self):
        head=self.head
        slow=None
        fast=head
        i=1
        j=1
        while(fast):
            if i*i==j:
                if not slow:
                    slow=head
                else:

                    slow=slow.next
                i+=1
            fast=fast.next        
            j+=1
        return slow.data

l=linkedlist()
l.insert(1)
l.insert(2)
l.insert(3)
l.insert(4)
l.insert(5)

l.insert(6)
l.insert(7)
l.insert(8)
l.insert(9)
print(l.RootNthNode())


