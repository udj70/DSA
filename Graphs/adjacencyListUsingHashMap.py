class graph:
    def __init__(self):
        self.dic={}
    def addEdge(self,x,y,bidir,wt):
        if x in self.dic:
            self.dic[x].append((y,wt))
        else:
            self.dic[x]=[]
            self.dic[x].append((y,wt))
        if bidir:
            if y in self.dic:
                self.dic[y].append((x,wt))
            else:
                self.dic[y]=[]
                self.dic[y].append((x,wt)) 
    def printList(self):
        for d in self.dic:
            print("vertex",d,"->",end=' ')
            for p in self.dic[d]:
                print(p[0],p[1],end=', ')
            print()            
g=graph()
g.addEdge("A","B",True,20)

g.addEdge("B","D",True,40)

g.addEdge("A","C",True,10)

g.addEdge("C","D",True,40)

g.addEdge("A","D",False,50)
g.printList()
