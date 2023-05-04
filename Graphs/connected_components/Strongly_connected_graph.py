#check if given directed graph is strongly connected
class graph:
    def __init__(self,v):
        self.v=v
        self.adj={}
        self.ssc=True
        self.time=0
    def addEdge(self,u,v):
        if u in self.adj:
            self.adj[u].append(v)
        else:
            self.adj[u]=[v]
        
    def DFS(self,u,visited,low):
        if not self.ssc:
            return False
        self.time+=1
        visited[u]=True
        curr_low=low[u]=self.time # current discovery time is low value of current node which will change later if their is any back edge
        if u in self.adj:
            for v in self.adj[u] :

                #if current adjacent is not visited then do DFS on it which will return it low value
                if not visited[v]:
                    curr_low=min(curr_low,self.DFS(v,visited,low)) # if low value of child is less then curr_low=child's low value
                
                #if current adjacent is visted that means their is any back or cross edge from u to v
                # hence new curr_low value is low[v] if it is less
                else:
                    curr_low=min(curr_low,low[v])
        
        #if u is not root and curr_low remain unchanged i.e no back edge found from any of its child to any of its ancestor 
        if u!=0 and curr_low==low[u]:
            self.ssc=False
        return curr_low    

    def IsSSC(self):
        visited=[False]*self.v

        # to keep track of lowest ancestor that can be reacheable from current node
        low=[self.time]*self.v 
        self.DFS(0,visited,low) #DFS from 0 
        
        #if in first DFS any node remain unvisted i.e is graph contain contain more then connected component
        for v in range(self.v):
            if not visited[v]:
                self.ssc=False
        if not self.ssc:
            print("graph is not strongly connected")
        else:
            print("Graph is strongly connected") 


g=graph(5)
g.addEdge(0,4)
g.addEdge(1,0)
g.addEdge(1,2)
g.addEdge(2,1)
g.addEdge(2,4)
g.addEdge(3,1)
g.addEdge(3,2)
g.addEdge(4,3)
'''g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(3,4)
g.addEdge(4,0)'''
g.IsSSC()
