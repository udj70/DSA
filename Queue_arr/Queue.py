#implementation of queue through array
class Queue_arr:
    def __init__(self):
        self.rear=-1
        self.front=-1
        self.q=[]
    def Isempty(self):
        if self.front==-1:
            return True
    def Enqueue(self,data):
        if self.front==-1:
            self.q.append(data)
            self.rear=self.front=0
        else:
            self.q.append(data)
            self.rear=self.rear+1
    def Dequeue(self):
        if self.front==-1:
            return 
        else:
            if self.front==self.rear:
                self.front=self.rear=-1
                return self.q.pop(self.front)
            else:
                self.front=self.front+1
                return self.q.pop(self.front-1)

