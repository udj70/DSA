class graph:
    def __init__(self):
        self.dic={}
        self.vis=[]
    def addEdge(self,x,y):
        if x in self.dic:
            self.dic[x].append(y)
        else:
            self.dic[x]=[]
            self.dic[x].append(y)
    def DFS(self,src):
        if src not in self.vis:
            print(src)
            self.vis.append(src)
        else:
            return   
        if src in self.dic:     
            for d in self.dic[src]:
                if d not in self.vis:
                    self.DFS(d)

g=graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(0,4)
g.addEdge(0,3)
g.addEdge(4,5)
g.addEdge(4,6)

g.DFS(0)              


