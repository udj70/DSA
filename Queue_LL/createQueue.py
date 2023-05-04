import node
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
    def IsEmptyQueue(self):
        return self.front==None    
    def Enqueue(self,obj):
        temp=node.Node(obj)
        
        if self.front==None:
            self.front=self.rear=temp
        else:
            self.rear.next=temp
            self.rear=temp
    def Dequeue(self):
        if self.IsEmptyQueue():
            print("empty Queue")
            return 
        elif self.front==self.rear:
             temp=self.front
             self.front=self.rear=None
             return temp.data
        else:
            temp=self.front
            self.front=self.front.next
            return temp.data     


