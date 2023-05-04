class graph:
    def __init__(self,v):
        self.v=v  
        self.edges=[]  #edge list
    def addEdge(self,u,v,w):
        self.edges.append((u,v,w))
    
    
    #find representative of set in which given node is present
    def find(self,parent,i):
        #if current node is parent of itself then it is representative 
        if parent[i]==i:
            return i
        #else recursivally call find function on parent of current node     
        return self.find(parent,parent[i]) 
    
    
    #union by rank
    def union(self,parent,rank,x,y):
       
        #whose rank will be more, it will be represenative of merged disjoints set
        if rank[x]<rank[y]:
            parent[x]=y
        elif rank[y]<rank[x]:
            parent[y]=x
        else:
            #if rank are equal then make any one as representative and increment the rank
            parent[y]=x
            rank[x]+=1
    def krushkalsMST(self):
        parent=[0]*self.v
        rank=[0]*self.v #current rank of every node is 0

        # every node is parent itself 
        for p in range(self.v):
            parent[p]=p
        resultSet=[]
        e=0

        #sort the edges on the basis of weights 
        self.edges=sorted(self.edges,key=lambda edge:edge[2])
        minWeight=0

        #min edges that a MSt will contain is v-1
        while(e<self.v-1):
            edge=self.edges.pop(0)
            u=edge[0]
            v=edge[1]
            w=edge[2]

            #find cureent reprensentative of each vertex of edge 
            x=self.find(parent,u)
            y=self.find(parent,v)
            #if  Rep of both are different then then include the edge in result set and
            #merge both vertex in same set
            if x!=y:
                e+=1
                resultSet.append((u,v))
                minWeight+=w
                self.union(parent,rank,x,y)
        return resultSet,minWeight

g = graph(4) 
g.addEdge(0, 1, 10) 
g.addEdge(0, 2, 6) 
g.addEdge(0, 3, 5) 
g.addEdge(1, 3, 15) 
g.addEdge(2, 3, 4) 
  
resultSet,minWeight=g.krushkalsMST()                 

for res in resultSet:
    print(res[0],"-",res[1])
print("Min weight",minWeight)    



