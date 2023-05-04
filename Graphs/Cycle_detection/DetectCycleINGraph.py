# approach-1 -can be solved by kahn algo also, maintain indegrees array, apply BFS, maintain counter whenwe acces node from queue,
# if counter become equal to N, so no edge, else there is edge(refere kahn's code just add counter)
# approach-2 -DFS approach
class graph:
    def __init__(self,V):
        self.V=V
        self.adj={}
    def addEdge(self,x,y):
        if x in self.adj:
            self.adj[x].append(y)
        else:
            self.adj[x]=[]
            self.adj[x].append(y)
    def isCyclicUtil(self,visited,dfs_visited,u):
        visited[u]=True
        dfs_visited[u]=True
        if u in self.adj:
            for v in self.adj[u]:
                if not visited[v]:
                   
                    if self.isCyclicUtil(visited,dfs_visited,v):
                        return True
                   
                elif dfs_visited[v]:
                    return True
        dfs_visited[u]=False
        return  False
    def isCyclic(self):
        visited=[False]*self.V

        #to check if node is visited in current dfs, if not i.e not cycle
        dfs_visited=[False]*self.V 
       
        
        for u in range(self.V):
            if not visited[u]:
                visited[u]=True
                dfs_visited[u]=True
                if u in self.adj:
                    for v in self.adj[u]:
                        if not visited[v]:
                            
                            if self.isCyclicUtil(visited,dfs_visited,v):
                                return True

                dfs_visited[u]=False
            elif dfs_visited[u]:
                return True
        return False



        

g=graph(8)
g.addEdge(0, 1);
g.addEdge(1,2);
g.addEdge(2,3);
g.addEdge(3,4);
g.addEdge(2,4);
g.addEdge(5,1);
g.addEdge(5,6);
g.addEdge(6,7);
g.addEdge(7,5);

'''g.addEdge(5, 2);
g.addEdge(5, 0);
g.addEdge(4, 0);
g.addEdge(4, 1);
g.addEdge(2, 3);
g.addEdge(3, 1);
'''
if g.isCyclic():
    print("graph contains cycle")
else:
    print("does not contain cycle")



