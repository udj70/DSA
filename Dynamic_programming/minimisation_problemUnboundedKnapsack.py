#hard coded solution of minimisatiopn problem on unbounded knapsack
#total weight=120
profit=[16,15]#profit array
weight=[6,8]#weight array

dp=[[0 for _ in range(121)] for _ in range(3)]
#make slight change in initialisation of dp from maximisation problem
#top row of dp will be inialized to infinity 
for i in range(1,121):
    dp[0][i]=float('inf')

for i in range(1,3):
    for j in range(1,121):
        if weight[i-1]<=j:
            dp[i][j]=min(dp[i][j-weight[i-1]]+profit[i-1],dp[i-1][j])
        else:
            dp[i][j]=dp[i-1][j]
print(dp[2][120])                    
