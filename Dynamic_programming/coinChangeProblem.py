#it is unbounded knapsack variant
# calculate total coin changes possible
# approach 1- recursive
def maximumNoOfWaysRecur(coins,i,target):
    if i < 0:
        return 0
    if target==0:
        return 1

    if coins[i]<=target:
        return maximumNoOfWays(coins,i,target-coins[i]) + maximumNoOfWays(coins,i-1,target)
    else:
        return maximumNoOfWays(coins,i-1,target)

# approach 2- memoise it
# approach 3- tabulation
def maximumNoOfWays(coins,s):
    dp=[[0 for _ in range(s+1)] for _ in range(len(coins)+1)]
    for i in range(len(coins)):
        dp[i][0]=1
    for i in range(1,len(coins)+1):
        for j in range(1,s+1):
            if coins[i-1]<=j:

                dp[i][j]=dp[i][j-coins[i-1]]+dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j]
    return dp[len(coins)][s] 
   
coins=[2,5,3,6]
print(maximumNoOfWays(coins,10))  


# space optimisation :)
