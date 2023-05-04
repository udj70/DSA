from collections import  defaultdict
#stack=[]
class graph:
    def __init__(self,V):
        self.V=V
        self.adj=defaultdict(list)
        self.indegree=[0]*self.V
    def addEdge(self,u,v):
        self.adj[u].append(v)
        self.indegree[v]+=1    
    def topologicalSortUtil(self,v,visited,stack):
        visited[v]=True
        
        for a in self.adj[v]:
            if not visited[a]:
                self.topologicalSortUtil(a,visited,stack)       
        stack.append(v)
    def topologicalSort(self):
        visited=[False]*self.V
        stack=[]
        for i in range(self.V):
            if not visited[i]:
                self.topologicalSortUtil(i,visited,stack)
        print(stack[::-1])
    def TLSBykahnAlgo(self):
        #print(self.indegree)
        queue=[]
        for i in range(self.V):
            if self.indegree[i]==0:
                queue.append(i)
        ans=[]
        while(len(queue)):
            n=queue.pop(0)
            ans.append(n)
            if n in self.adj:
                for v in self.adj[n]:
                    self.indegree[v]-=1
                    if self.indegree[v]==0:
                        queue.append(v)
        print(ans)                        

g= graph(8) 
# g.addEdge(5, 2) 
# g.addEdge(5, 0) 
# g.addEdge(4, 0) 
# g.addEdge(4, 1) 
# g.addEdge(2, 3) 
# g.addEdge(3, 1) 

g.addEdge(0, 1);
g.addEdge(1,2);
g.addEdge(2,3);
g.addEdge(3,4);
#g.addEdge(2,4);
g.addEdge(5,1);
g.addEdge(5,6);
g.addEdge(6,7);
#g.addEdge(7,5)
  
print("Following is a Topological Sort of the given graph")
g.topologicalSort()   
g.TLSBykahnAlgo()     

