#work on concept of inserting intermediate vertex in current path and check whether curent direct path 
# or path through given intermediate is smaller 
def ShortestPath(graph):
    n=len(graph)
    for k in range(n): # for every intermediate vertex [0,1,2,3,4....len(graph)]
        #traverse the graph and check min of current path and path after inserting intermediate vertex
        for i in range(n):
            for j in range(n):
                #current indermediate vertex row and column will remain unchanged and 
                #diagonal will be zero always as there is no path to itself directly( no self loops)
                graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])
    return graph
inf=float('inf')
graph=[[0,3,inf,7],
        [8,0,2,inf],
        [5,inf,0,1],
        [2,inf,inf,0]] 
print(ShortestPath(graph))   

#output->[[0, 3, 5, 6], 
#         [5, 0, 2, 3], 
#         [3, 6, 0, 1], 
#         [2, 5, 7, 0]]

#TC->O(V^3)