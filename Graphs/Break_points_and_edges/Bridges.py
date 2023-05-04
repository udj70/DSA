
#same as articulation point logic just difference 
# we have to find an edge which if removed will lead 
# to increase in number of disconnected components 
#for this to happen edge u-v should satisfy the condition low[v]>disc[u]

class graph:
    def __init__(self,V):
        self.v=V
        self.adj={}
        self.time=0
    def addEdge(self,u,v):
        if u in self.adj:
            self.adj[u].append(v)

        else:
            self.adj[u]=[v]
        if v in self.adj:
            self.adj[v].append(u)
            
        else:
            self.adj[v]=[u]    
    def BridgeUtil(self,u,visited,parent,disc,low):
        self.time+=1
        visited[u]=True
        disc[u]=low[u]=self.time
        #children=0
        if u in self.adj:
            for v in self.adj[u]:
                if not visited[v]:
                    #children+=1
                    parent[v]=u
                    self.BridgeUtil(v,visited,parent,disc,low)

                    low[u]=min(low[u],low[v])
                    if low[v]>disc[u]:
                        print(u,"-",v)
                elif parent[u]!=v:
                    low[u]=min(low[u],disc[v])             


    def Bridge(self):
        visited=[False]*self.v
        parent=[-1]*self.v
        disc=[0]*self.v
        low=[0]*self.v
        #ap=[False]*self.v
        for v in range(self.v):
            if not visited[v]:
                self.BridgeUtil(v,visited,parent,disc,low)
        
g1=graph(5)
print("\nBridges in first graph ")

g1.addEdge(1, 0)
g1.addEdge(0, 2)
g1.addEdge(2, 1)
g1.addEdge(0, 3)
g1.addEdge(3, 4)
#print(g1.adj[1])
g1.Bridge()

print("\nBridges in second graph")
g2=graph(4)
g2.addEdge(0, 1)
g2.addEdge(1, 2)
g2.addEdge(2, 3)
g2.Bridge()

print("\nBridges  in third graph ")
g3=graph(7)
g3.addEdge(0, 1)
g3.addEdge(1, 2)
g3.addEdge(2, 0)
g3.addEdge(1, 3)
g3.addEdge(1, 4)
g3.addEdge(1, 6)
g3.addEdge(3, 5)
g3.addEdge(4, 5)
g3.Bridge()
