# condition- It should be directed graph

class graph:
    def __init__(self,V):
        self.V=V
        self.edgeList=[]
        self.E=0
    def addEdge(self,u,v,w):
        self.edgeList.append([u,v,w])
    def BellmanFord(self):
        self.E=len(self.edgeList)
        v=self.V
        e=self.E
        edgeList=self.edgeList
        max_size=float('inf')
        dist=[max_size]*v

        dist[0]=0
        for i in range(v-1):
            for j in range(e):
                if dist[edgeList[j][1]]>dist[edgeList[j][0]]+edgeList[j][2]:
                     dist[edgeList[j][1]]=dist[edgeList[j][0]]+edgeList[j][2]
        #check for negative weight cycle
        for i in range(v-1):
            for j in range(e):
                if dist[edgeList[j][1]]>dist[edgeList[j][0]]+edgeList[j][2]:
                     #dist[edgeList[j][1]]=dist[edgeList[j][0]]+edgeList[j][2]
                     print("graphs contain negative weight cycle")
                     return
        print(dist)
        return 
g=graph(4)
'''g.addEdge(0,1,-1)
g.addEdge(0,2,4)
g.addEdge(1,2,3)

g.addEdge(1,3,2)
g.addEdge(1,4,2)
g.addEdge(3,2,5)
g.addEdge(3,1,1)
g.addEdge(4,3,-3)
'''
g.addEdge(0,1,1)
g.addEdge(1,2,-1)
g.addEdge(2,3,-1)

g.addEdge(3,0,-1)
g.BellmanFord()
                     


                     



