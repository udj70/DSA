def issafe(i,j,r,c):
    if i<r and i>=0 and j<c and j>=0:
        return True
    return False    
def IsPossibleToRottten(arr):   #BFS approach
    directions=[(0,-1),(0,1),(1,0),(-1,0)] # all four direction that a orange can rot
    q=[] #queue for executing BFS
    fresh=[]
    #add all rotten orange coordinates with it current time frame i.e 0 to queue and fresh oranges to fresh[] array
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j]==2:
                q.append((i,j,0))
            elif arr[i][j]==1:
                fresh.append((i,j))
              
    time=0            
    # for each dequed rotten arrange check whether it can rot any of its adjacent and append that adjacent to queue 
    # with time frame 1 more than the current orange time frame and replace that adjacent current value with 
    # 2(marking it as rotten)
    while(len(q)!=0):

        rotten=q.pop(0)
        for d in directions:
            if issafe(rotten[0]+d[0],rotten[1]+d[1],len(arr),len(arr[0])) and arr[rotten[0]+d[0]][rotten[1]+d[1]]==1:
                arr[rotten[0]+d[0]][rotten[1]+d[1]]=2 # mark current adjacent rotten
                q.append((rotten[0]+d[0],rotten[1]+d[1],rotten[2]+1))
                fresh.remove((rotten[0]+d[0],rotten[1]+d[1]))  # remove current rotten orange from fresh oranges
        time=rotten[2]  # current poped elemnt time frame      
    if len(fresh)!=0: # non empty fresh orange array 
        return -1
    return time # if there is no fresh oranges then return last poped elemnt time frame

arr=[ [2, 1, 0, 2, 1],
    [1, 0, 0, 2, 1],
    [1, 0, 0 , 2, 1]]
print(IsPossibleToRottten(arr)) #2 time frames

