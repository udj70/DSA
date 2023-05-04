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
    def tail(self):
        temp=self.head
        while(temp.next):
            temp=temp.next
        return temp
    def createLoop(self,tail):
        temp=self.head
        count=0
        prev=None
        while(temp.next and count<3):
            prev=temp
            temp=temp.next
            count+=1
        tail.next=prev
    def detectLoop(self):
        slow=self.head
        fast=self.head
        while(fast.next and fast.next.next):
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                print("loop present")
                break
        return  
    def loopPosition(self):
        slow=self.head
        fast=self.head
        while(fast.next and fast.next.next):
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                break
        slow=self.head
        while(slow!=fast):
              slow=slow.next
              fast=fast.next
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
tail=l.tail()
l.createLoop(tail)
l.detectLoop()
print(l.loopPosition())

