class graph:
    def __init__(self):
        self.dic={}
    def addEdge(self,x,y):
        if x in self.dic:
            self.dic[x].append(y)
        else:
            self.dic[x]=[]
            self.dic[x].append(y)
    def BFS(self,src): 
        vis={}
        q=[]
        q.append(src)
        vis[src]=True
        while(len(q)):
            node=q.pop(0) 
            print(node)
            if node in self.dic:
                for nbr in self.dic[node]:
                    if nbr not in vis:
                        vis[nbr]=True
                        q.append(nbr) 
g=graph()
g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(3,4)
g.addEdge(4,5) 

g.BFS(0)              

    
    
