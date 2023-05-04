#push operation costly



class stack:
    def __init__(self):
        
        self.q1=[]
        self.q2=[]
    def pop(self):
        self.q1.pop(0)
    def push(self,data):
        while(len(self.q1)):
            self.q2.append(self.q1.pop(0))
        self.q1.append(data)
        while(len(self.q2)):
            self.q1.append(self.q2.pop(0)) 
s=stack()
s.push(3)
s.push(4)
s.push(5)
s.pop()
print(s.q1)



#pop operation costly
class stack2:
    def __init__(self):
        self.q1=[]
        self.q2=[]
    def pop(self):
        while(len(self.q1)>1):
            self.q2.append(self.q1.pop(0))
        self.q1.pop(0)
        while(len(self.q2)):
            self.q1.append(self.q2.pop(0))
    def push(self,data):
        self.q1.append(data)

s=stack2()
s.push(3)
s.push(4)
s.push(5)
s.pop()
print(s.q1)    

#pop operation costly but using single queue (just simply push front (n-1) elemnt back into same queue not in other)
class stack3:
    def __init__(self):
        self.q1=[]
    def pop(self):
        i=0
        while(i<len(self.q1)-1):
            self.q1.append(self.q1[0])
            self.q1.pop(0)
            i+=1
        self.q1.pop(0)    
       
    def push(self,data):
        self.q1.append(data)

s=stack3()
s.push(3)
s.push(4)
s.push(5)
s.pop()
print(s.q1)    





