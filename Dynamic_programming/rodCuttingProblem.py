#same as unbounded knapsack problem
def maxProfitInRodCutting(lengths,values,rLength):
    dp=[[0 for _ in range(rLength+1)] for _ in range(len(lengths)+1)]
    for i in range(len(lengths)+1):
        for j in range(rLength+1):
            if lengths[i-1]<=j:
                dp[i][j]=max(values[i-1]+dp[i][j-lengths[i-1]],dp[i-1][j])
            else:
                dp[i][j]=dp[i-1][j]
    return dp[len(lengths)][rLength]
lengths =[1,2,   3,   4 ,  5 ,  6 ,  7 ,  8  ]   
values  =[ 1 , 5,   8,   9 , 10,  17,  17,  20]     
print(maxProfitInRodCutting(lengths,values,8))        

