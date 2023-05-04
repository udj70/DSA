# it is used in case when edge weights is not unit, other wise in case of unit weight we can simple apply BFS usising queue
# can be used on diredted or undirected graph 
import heapq
class graph:
    def __init__(self,num):
        self.dic={}
        self.weight=[float('inf')]*num
    def addEdge(self,u,v,d):
        if u in self.dic:
            self.dic[u].append((v,d))
        else:
            self.dic[u]=[]
            self.dic[u].append((v,d))
        '''if v in self.dic:
            self.dic[v].append((u,d))
        else:
            self.dic[v]=[]
            self.dic[v].append((u,d)) 
        '''       
    def shortest_path(self,u):
        queue=[]
        self.weight[u]=0

        queue.append((self.weight[u],u))
        heapq.heapify(queue)
        
        while(len(queue)!=0):
            v=heapq.heappop(queue)
            print(v)
            if v[1] in self.dic:
                for adj in self.dic[v[1]]:
                    if self.weight[adj[0]]>v[0]+adj[1]:
                        self.weight[adj[0]]=v[0]+adj[1]

                        #after updating current adj, put that in heap    
                        heapq.heappush(queue,(self.weight[adj[0]],adj[0]))
                   
                   
                    '''vertex=adj[0]
                    weight=adj[1]
                    self.weight[vertex]=min(self.weight[vertex],self.weight[v[1]]+weight)
                    heapq.heappush(queue,(self.weight[vertex],vertex))
                    '''




g=graph(7)
'''g.addEdge( 0, 1, 4); 
g.addEdge( 0, 7, 8); 
g.addEdge( 1, 2, 8); 
g.addEdge( 1, 7, 11); 
g.addEdge( 2, 3, 7); 
g.addEdge( 2, 8, 2); 
g.addEdge( 2, 5, 4); 
g.addEdge( 3, 4, 9); 
g.addEdge( 3, 5, 14); 
g.addEdge( 4, 5, 10); 
g.addEdge( 5, 6, 2); 
g.addEdge( 6, 7, 1); 
g.addEdge( 6, 8, 6); 
g.addEdge( 7, 8, 7);'''
g.addEdge(1,2,2)
g.addEdge(1,3,4)
g.addEdge(2,3,1)
g.addEdge(2,4,7)
g.addEdge(3,5,3)
g.addEdge(4,6,1)

g.addEdge(5,6,5)
g.addEdge(5,4,2)
g.shortest_path(1)   
print(g.weight)                  