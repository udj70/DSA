#enqueue operation costly

class queue:
    def __init__(self):
        self.s1=[]
        self.s2=[]
    def enqueue(self,data):
        while(len(self.s1)):
            self.s2.append(self.s1.pop())
        self.s1.append(data)
        while(len(self.s2)):
            self.s1.append(self.s2.pop())
    def dequeue(self):
        self.s1.pop()
q=queue()
q.enqueue(3)
q.enqueue(4)
q.enqueue(5) 
q.dequeue()
q.enqueue(6)
q.dequeue()
print(q.s1)    



#deqeue operation costly TC-O(N) because of pop operation
class queue1:
    def __init__(self):
        self.s1=[]
        self.s2=[]
    def enqueue(self,data):
        self.s1.append(data)
    def dequeue(self):
        while(len(self.s1)>1):
            self.s2.append(self.s1.pop())
        self.s1.pop()
        while(len(self.s2)):
            self.s1.append(self.s2.pop())
q=queue1()
q.enqueue(3)
q.enqueue(4)
q.enqueue(5) 
q.dequeue()
q.enqueue(6)
q.dequeue()
print(q.s1)    

#dequeue operation costly but optimised, amortised TC(O(1))
class queue2:
    def __init__(self):
        self.s1=[]
        self.s2=[]
    def enqueue(self,data):
        self.s1.append(data)
    def dequeue(self):
        if(not len(self.s2)):
            while(len(self.s1)):
                self.s2.append(self.s1.pop())
        self.s2.pop()
        
q=queue2()
q.enqueue(3)
q.enqueue(4)
q.enqueue(5) 
q.dequeue()
q.enqueue(6)
q.dequeue()
print(q.s1,q.s2)              