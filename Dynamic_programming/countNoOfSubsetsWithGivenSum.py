def countSubs(arr,s):
    dp=[[0 for _ in range(s+1)] for _ in range(len(arr)+1)]
    for i in range(len(arr)+1):
        dp[i][0]=1
    for i in range(1,len(arr)+1):
        for j in range(1,s+1):
            if arr[i-1]>j:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j]+dp[i-1][j-arr[i-1]]
    return dp[len(arr)][s]
arr=[2,3,5,6,8,10]
print(countSubs(arr,10))                    

