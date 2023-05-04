class graph:
    def __init__(self,v):
        self.adj={}
        self.v=v
        self.ans=float('inf')
    def addedge(self,u,v,w):
        if u in self.adj:
            self.adj[u].append((v,w))
           
        else:
            self.adj[u]=[(v,w)]
        if v in self.adj:
            self.adj[v].append((u,w))
           
        else:
            self.adj[v]=[(u,w)]
    def dfs(self,visited,u,dis,destination,k):
        if u==destination:
            dis.sort()
            self.ans=min(self.ans,sum(dis[:len(dis)-k]))
            #print('h')
            #print(dis)
            return 
        if u in self.adj:
            for pair in self.adj[u]:
                v=pair[0]
                weight=pair[1]
                if not visited[v]:
                    visited[v]=True
                    dis.append(weight)
                    self.dfs(visited,v,dis,destination,k)
                    visited[v]=False
                    dis.pop()
        return
g=graph(5)
g.addedge(0,4,1)
g.addedge(4,3,7)
g.addedge(0,1,1)
g.addedge(1,2,2)
g.addedge(2,3,4)
#g.addedge(1,3,8)
visited=[False]*g.v
source=0
destination=3
k=1
dis=[]
visited[0]=True
g.dfs(visited,source,dis,destination,k)
print(g.ans)

                       



            
