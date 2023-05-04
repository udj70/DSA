def minKey(key,mstSet,V):
    m=float('inf')
    min_index=-1
    for v in range(V):
        if not mstSet[v] and key[v]<m:
            m=key[v]
            min_index=v
    return min_index         

def minSpanningTree(adj):
    V=len(adj)
    mstSET=[False]*V
    key=[float('inf')]*V  #it is current minimum distance of that vertex from any of it vertex already included in mstSET
    key[0]=0 
    parent=[-1]*V 
    for _ in range(V-1):
        u=minKey(key,mstSET,V) #fetch mininmum key from mstSET in O(V) time(can use min heap to reduce complexity to logV)
        mstSET[u]=True  #mark the current vertex as visited or included in mstSET
        
        for v in range(V): #traverse all its adjacent and add the current edge weight as key value of that adjacent
            if adj[u][v] and not mstSET[v] and adj[u][v]<key[v]:
                key[v]=adj[u][v]
                parent[v]=u
    for v in range(1,V):
        print(parent[v],'-',v,'--> ',key[v])
adj=[ [ 0, 2, 0, 6, 0 ], 
        [ 2, 0, 3, 8, 5 ], 
        [ 0, 3, 0, 0, 7 ], 
        [ 6, 8, 0, 0, 9 ], 
        [ 0, 5, 7, 9, 0 ]]
minSpanningTree(adj)                         

    

