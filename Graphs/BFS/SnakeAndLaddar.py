#task- find min moves to reach the end of snake and laddar board
# approach- start from 0, and check for all six dice throws, update cell visisted by those new positions and jumps to reach them

#function will accept moves array and number of cells in board
def SnakeAndLaddar(moves,N):
    #mark all cell initally as unvisited
    visited=[False]*N

    #we will perform BFS at each cell of board and check for new position reacheable in 6 diffent dic through
    #create a queue for BFS
    q=[]

    #insert first tuple in queue with data current cell number and
    #minimum dice throughs to reach at this cell i.e minimum distance
    q.append((0,0)) #current cell number=0,dist=0
    visited[0]=True
    while(len(q)):
        cell=q.pop(0)
        cell_no=cell[0]
        dist=cell[1]

        #if current cell number is last cell i.e destination, 
        # break the loop and return current dist as minimum dice throws required
        if cell_no==N-1:
            ans=dist
            break
        #if not then check for all 6 dice throws and mark the position reachable
        j=cell_no+1
        while(j<=cell_no+6 and j<N):

            #if current cell is not visited then only update it with new values else continue 
            if not visited[j]:
                #mark Jth position ans visited
                visited[j]=True
                #new dist to reach this cell is current dist+1
                new_dist=dist+1
                #new cell that will be reached will be cell number provide in moves
                # array corresponding to that J index 
                new_cell=moves[j] if moves[j]!=-1 else j
                #add the current cell details as tuple in queue
                q.append((new_cell,new_dist))
            j+=1        

    return ans



N = 30
#we are given a snake and laddar board
#intialize the move from each cell to -1

moves = [-1] * N 
  
# Ladders 
moves[2] = 21
moves[4] = 7
moves[10] = 25
moves[19] = 28
  
# Snakes 
moves[26] = 0
moves[20] = 8
moves[16] = 3
moves[18] = 6
print(SnakeAndLaddar(moves,N))  



def snl(moves,N):
    queue=[]
    visited=[False]*N
    queue.append((0,0))
    while(len(queue)):
        cell=queue.pop(0)
        cell_no=cell[0]
        dist=cell[1]
        j=cell_no+1

        if cell_no==N-1:
            ans=dist
        while(j<=cell_no+6 and j<N):
            if not visited[j]:
                visited[j]=True
                new_cell=moves[j] if moves[j]!=-1 else j
                new_dist=dist+1
                queue.append((new_cell,new_dist))
            j+=1

