#calculate the sum of rectangle between the mentioned coordinates 
#for that we have to preprocess the 2D array to from new dp array
def rectangularSum(arr):
    m=len(arr)
    n=len(arr[0])
    dp=[[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            dp[i][j]=dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]+arr[i-1][j-1]
    return dp



arr=[[2,0,-3,4],[6,3,2,-1],[5,4,7,3],[2,-6,8,1]]
q_lis=[[0,0,2,2],[1,1,2,2],[2,2,2,2]]
dp=rectangularSum(arr)
print(dp)
for q in q_lis:
    x1=q[0]
    y1=q[1]
    x2=q[2]
    y2=q[3]
    #now calculating the sum in the given range in O(1) time from dp array
    sum=dp[x2+1][y2+1]-dp[x1][y2+1]-dp[x2+1][y1]+dp[x1][y1]
    print('(',x1,',',y1,') ','-> ','(',x2,',',y2,') ','sum is',sum)



