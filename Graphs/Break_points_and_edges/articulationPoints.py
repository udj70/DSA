#tarjan's algorithm


class graph:
    def __init__(self,V):
        self.v=V
        self.adj={}
        self.time=0 #for calculating discorvery time of every node in dfs
    def addEdge(self,u,v):
        #undirected graph
        if u in self.adj:
            self.adj[u].append(v)

        else:
            self.adj[u]=[v]
        if v in self.adj:
            self.adj[v].append(u)
            
        else:
            self.adj[v]=[u]    
    def ApUtil(self,u,visited,parent,disc,low,ap):
        self.time+=1 #as we visit any node then increment the time 
        visited[u]=True
        disc[u]=low[u]=self.time # current node discovery time and low value will be same as time 
        children=0 #intialse children and as the adjacent nodes are visted increment the children count
        if u in self.adj:
            for v in self.adj[u]:
                if not visited[v]:
                    #increment children
                    children+=1 
                    parent[v]=u
                    #DFS on child node
                    self.ApUtil(v,visited,parent,disc,low,ap) 
                    
                    # after DFS on u's adjacent v redefine the low value of u,
                    #i.e lowest ancestor recheable by v is less than the lowest ancestor recheable by u, low[u]=low[v]
                    
                    low[u]=min(low[u],low[v])          
                    
                    #1.) u is root then check if number of children of u is more then 1, if it is so then u is articulation point
                    if parent[u]==-1 and children>1:
                        ap[u]=True
                    #2.) u is not root and lowest anncestor recheable by v is more than discovery time of u, then their is no back edge, hence u s articulation point

                    if parent[u]!=-1 and low[v]>=disc[u]:
                        ap[u]=True

                elif parent[u]!=v: #if current adjacent is not parent of current node(this can be possible coz it is undirected graph), the their is back edge and low value of u will be discovery time of v 
                    low[u]=min(low[u],disc[v])             


    def Ap(self):
        visited=[False]*self.v
        parent=[-1]*self.v
        disc=[0]*self.v #discovery time of each node
        low=[0]*self.v # lowest ancestor's discovery time which recheable by current node
        ap=[False]*self.v # whethe rcurrent node is ap or not
        for v in range(self.v):
            if not visited[v]:
                self.ApUtil(v,visited,parent,disc,low,ap)
        for a in range(self.v):
            if ap[a]:
                print(a,end=' ')


print("\nArticulation points in first graph \n")
g1=graph(5)

g1.addEdge(1, 0)
g1.addEdge(0, 2)
g1.addEdge(2, 1)
g1.addEdge(0, 3)
g1.addEdge(3, 4)
#print(g1.adj[1])
g1.Ap()

print("\nArticulation points in second graph \n")
g2=graph(4)
g2.addEdge(0, 1)
g2.addEdge(1, 2)
g2.addEdge(2, 3)
g2.Ap()

print("\nArticulation points in third graph \n")
g3=graph(7)
g3.addEdge(0, 1)
g3.addEdge(1, 2)
g3.addEdge(2, 0)
g3.addEdge(1, 3)
g3.addEdge(1, 4)
g3.addEdge(1, 6)
g3.addEdge(3, 5)
g3.addEdge(4, 5)
g3.Ap()

