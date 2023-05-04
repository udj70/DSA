#task- given DAG find shortest path to all nodes
# approach- perform topological sort, save the ans, now traverse sorted array, and apply DFS from each node, and update distance
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
    def topological_sort(self,u,visited,stack):
        visited[u]=True

        if u in self.adj:
            for v in self.adj[u]:
                if not visited[v]:
                    self.topological_sort(v,visited,stack)
        stack.append(u)

    def shortest_path_in_DAG(self):
        visited=[False]*self.V
        stack=[]
        for v in range(self.V):
            if not visited[v]:
                self.topological_sort(v,visited,stack)
        #print(stack[::-1])
        dist=[float('inf')]*self.V
        while(len(stack)):
            node=stack.pop()
            # all outgoing edges present, so distance of this node will be 0
            if dist[node]==float('inf'):
                dist[node]=0
            # visit current adjacent of node, and update there distance
            if node in self.adj:
                for neighbor in self.adj[node]:
                    if dist[node]+1<dist[neighbor]:
                        dist[neighbor]= dist[node]+1
        print(dist)
g=graph(8)
g.addEdge(0, 1);
g.addEdge(1,2);
g.addEdge(2,3);
g.addEdge(3,4);
#g.addEdge(2,4);
g.addEdge(5,1);
g.addEdge(5,6);
g.addEdge(6,7);
#g.addEdge(7,5)

g.shortest_path_in_DAG()