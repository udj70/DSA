class graph:
    def __init__(self,V):
        self.V=V
        self.dic={}
        self.visited=[False]*self.V
    def addEdge(self,u,v):
        if u in self.dic:
            self.dic[u].append(v)
        else:
            self.dic[u]=[v]
        if v in self.dic:
            self.dic[v].append(u)
        else:
            self.dic[v]=[u]
    def DFS(self,v):
        print(v,end=' ')
        self.visited[v]=True
        if v in self.dic:
            for d in self.dic[v]:
                if not self.visited[d]:
                    self.DFS(d)            
    def connectedComponent(self):
        #visited=[False]*self.V
        i=1
        for d in self.dic:
           
            if not self.visited[d]:
                print("connected component",i)
                i+=1
               
                self.DFS(d)  
                print()
                  
           
g=graph(5) 
g.addEdge(1, 0)
g.addEdge(1, 2)
g.addEdge(3, 4) 
g.connectedComponent()                              

