#refer prateek narang video
# tc- O((2^n) * n), sc=O(2^n * n) here 2^n is all possible mask conbinations, ex, n=3, 8 combinations 000 to 111
adj=[[0,20,42,25],[20,0,30,34],[42,30,0,10],[25,34,10,0]]
dp=[[-1]*4 for _ in range(16)] # dp to store result shortest path from  current node
n=4
visited_all=(1<<n)-1
def tsp(mask,pos):
    ans=float('inf')
    if dp[mask][pos] !=-1:
        return dp[mask][pos]
   
    if mask==visited_all:
        return adj[pos][0] #reaching back to origin from current position
    #else try to go to all none visited cites
    for city in range(n):
        if not  (mask & (1<<city)): # ex- mask- 0110, create temp mask 1<<city i.e 0100, perform bitwse and, 
                                    # if it is non zero, so current city is visisted
            
            # when we pick the city, so update mask, just perform bitwise or rather than and in previous formula
            # current mask- 0110, and current city is 3, (0110) | (1000)=1110, here 1000 is 1<<city
            # ad cost to reach curr city adj[pos][city] and make recursive call on remaining city
            newans=adj[pos][city]+tsp(mask | (1<<city),city) 

            ans=min(ans,newans)
    dp[mask][pos]=ans
    return ans        


print(tsp(1,0))
