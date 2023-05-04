#task- find shortest path to each node in undirected graph, if each edge have unit weights
# approach- simply do BFS in updated distance of node, if it is not checked or if it is smaller then previous value

#refere strivers channel
class graph:
    def __init__(self,V):
        self.V=V
        self.adj={}
    def addEdge(self,x,y):
        if x in self.adj:
            self.adj[x].append(y)
        else:
            self.adj[x]=[y]
        if y in self.adj:
            self.adj[y].append(x)
        else:
            self.adj[y]=[x]
    def BFS_to_shortest_distance(self):
        dist=[float('inf')]*self.V
        dist[0]=0

        queue=[0]
        while(len(queue)):
            node=queue.pop(0)
            if node in self.adj:
                for neighbour in self.adj[node]:
                    if dist[node]+1<dist[neighbour]:
                        dist[neighbour]= dist[node]+1
                        queue.append(neighbour)
        print(dist)
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

g.BFS_to_shortest_distance()