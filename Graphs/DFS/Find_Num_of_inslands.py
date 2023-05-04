#It checks weather at given index it is 1 or not and i,j in range of col and rows 
def issafe(M,i,j):
    col=len(M[0])
    row=len(M)
    if i<row and i>=0 and j<col and j>=0 and M[i][j]:
        return True
    return False    
#for given non visited index check for all its 8 neighbours which contains 1 and mark them visted recursively    
def DFS(M,i,j,visited):
    visited[i][j]=True
    #all possible sums for 8 neighbours for any in index
    rowNbr=[-1, -1, -1, 0, 0, 1, 1, 1]
    colNbr=[-1, 0, 1, -1, 1, -1, 0, 1]
    for k in range(8):
        if issafe(M,i+rowNbr[k],j+colNbr[k]) and not visited[i+rowNbr[k]][j+colNbr[k]]:
            DFS(M,i+rowNbr[k],j+colNbr[k],visited)
#count number of disjoints islands
def countNumIslands(M):
    col=len(M[0])
    row=len(M)
    visited=[[False for _ in range(col)] for _ in range(row)]
    count=0
    for i in range(row):
        for j in range(col):
            if not visited[i][j] and M[i][j]:
                DFS(M,i,j,visited)
                count+=1            
    return count
M= [[1,  1, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1]]
print(countNumIslands(M))  #5 islands      
