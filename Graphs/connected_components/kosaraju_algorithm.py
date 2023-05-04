class graph:
    def __init__(self,V):
        self.V=V
        self.adj={}
    def addEdge(self,u,v):
        if u in self.adj:
            self.adj[u].append(v)
        else:
            self.adj[u]=[v]

    def fillStack(self,u,stack,visited):
        visited[u]=True
        if u in self.adj:
            for v in self.adj[u]:
                if not visited[v]:
                    self.fillStack(v,stack,visited)
        stack.append(u)
    def reverse(self):
        rev={}
        #reversing the mapping from value to key
        for a in self.adj:
            for el in self.adj[a]:
                if el in rev:
                    rev[el].append(a)
                else:
                    rev[el]=[a]
        return rev                     
    def DFS(self,u,visited,rev):
        visited[u]=True
        print(u,end=' ')
        if u in rev:
            for v in rev[u]:
                if not visited[v]:
                    self.DFS(v,visited,rev)


    def printSCC(self):
        stack=[] #use of stack to store visted vertices whose adjacent vertices are also visited in same way as used in topological sorting

        #simple DFS logic with vertices stored in stack   
        visited=[False]*self.V
        for v in range(self.V):
            if not visited[v]:
                self.fillStack(v,stack,visited)
        
        #reversal of graph by reversing the adjacency list
        rev=self.reverse()

        #simple DFS of reversed graph
        visited=[False]*self.V
        while(len(stack)!=0):
            v=stack.pop()
            if not visited[v]:
                self.DFS(v,visited,rev)
                #one strongly connected component is accessed, then change line
                print()
g=graph(5)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(0, 3)
g.addEdge(3, 4)

g.printSCC()

#TC=O(V+E), becoz first we fillstack by performing DFS in O(V+E),
#then perform reversal of adjacency list in O(V+E) time,
# then again DFS on reversed graph in O(V+E) time
                      

