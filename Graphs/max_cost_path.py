class graph:
    def __init__(self):
        self.adj={}
    def addEdge(self,u,v,w):
        if u in self.adj:
            self.adj[u].append((v,w))
        else:
            self.adj[u]=[(v,w)]
        if v in self.adj:
            self.adj[v].append((u,w))
        else:
            self.adj[v]=[(u,w)]
    def BFS_to_max_cost_path(self,src,k):
        queue=[(0,0,[src])]
        maxCost=0
        while(len(queue)):
            edge=queue.pop(0)
            u=edge[0]
            curr_cost=edge[1]
            visited=edge[2]
            if curr_cost>k:
                maxCost=max(maxCost,curr_cost)
            if u in self.adj:
                for v in self.adj[u]:
                    if v[0] not in visited:
                        s=[]
                        s=s+visited
                        s.append(v[0])
                        #visited.append(v[0])
                        queue.append((v[0],curr_cost+v[1],s))
        return maxCost
g=graph()                       
#g.addEdge()

g.addEdge(0, 6, 11) 
g.addEdge(0, 1, 5)
g.addEdge(1, 6, 3) 
g.addEdge(1, 5, 5) 
g.addEdge(1, 2, 7)
g.addEdge(2, 3, -8) 
g.addEdge(3, 4, 10) 
g.addEdge(5, 2, -1)
g.addEdge(5, 3, 9) 
g.addEdge(5, 4, 1)
g.addEdge(6, 5, 2) 
g.addEdge(7, 6, 9) 
g.addEdge(7, 1, 6)
print(g.BFS_to_max_cost_path(0,21))






                                