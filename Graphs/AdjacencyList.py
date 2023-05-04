class graph:
    def __init__(self,v):
        self.v=v
        self.lis=[[] for _ in range(v)]
    def add_edge(self,x,y):
        self.lis[x].append(y)
        self.lis[y].append(x)
g=graph(4)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(2,3)
g.add_edge(1,2)
for l in range(len(g.lis)):
    print("vertex",l,"-> ",",".join(map(str,g.lis[l])))       
