#two operation-find and union
#modification->find and path compression
            #->union by rank

def find(parent,i):
    if parent[i]==-1:
        return i
    return find(parent,parent[i])
  
#TC<O(logV)~constant becoz of path compression
def findAndPathCompression(parent,i):
    if parent[i]==-1:
        return i
    parent[i]=find(parent,parent[i])    

    return parent[i]


def union(parent,x,y):
    parent[x]=y


def unionByRank(parent,rank,x,y):
    if rank[x]>rank[y]:
        parent[y]=x 
    elif rank[y]>rank[x]:
        parent[x]=y
    else:

        parent[y]=x
        rank[x]+=1           


def detectCycle(edges,v):
    parent=[-1]*v 
    #edges=sorted(edges,key=lambda item:item[2])
    for e in edges:
        u=e[0]
        v=e[1]
        x=find(parent,u) #can also use findAndPathCompression()
        y=find(parent,v) 
        if x==y:
            #print("graph contain cycle")
            return True
            
        else:
            union(parent,x,y) #can also use unionByRank()
    return False
edges=[(0,1),(2,3),(1,2),(3,0)] #3-0 makes a cycle
v=4
if detectCycle(edges,v):
    print("graph contain cycle")
else:
    print("no cycle")        




