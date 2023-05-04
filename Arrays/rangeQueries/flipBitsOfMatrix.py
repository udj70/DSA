'''def flipBits(arr,q_lis):
    m=len(arr)
    n=len(arr[0])
    dp=[[0 for _ in range(n+1)] for _ in range(m+1)]
    for q in q_lis:
        x1=q[0]-1
        y1=q[1]-1
        x2=q[2]-1
        y2=q[3]-1
        
        dp[x2+1][y2+1]+=1
        dp[x1][y1]+=1
        dp[x1][y2+1]-=1
        dp[x2+1][y1]-=1
           
    for i in range(1,m+1):
        for j in range(1,n+1):
            dp[i][j]=dp[i][j]+dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]
            if dp[i][j]%2!=0:
                arr[i-1][j-1]=arr[i-1][j-1]^1  
    print(dp)             
    return arr


#input matrix
arr=[[0,0],
    [0,0]]
#flip the bits in the given ranges
q_lis=[[1,1 ,2 ,2],
        [1,1 ,2 ,2],
        [1,1 ,2 ,2] ]
arr=flipBits(arr,q_lis)
for a in arr:
    print(a)
'''

# Function to modify dp[][] array by
# generating prefix sum
def modifyDP(matrix, dp):
	
	for j in range(1, len(matrix)+1):
		
		for k in range(1, len(matrix[0])+1):
			
			# Update the tabular data
			dp[j][k] = dp[j][k] + dp[j-1][k] + dp[j][k-1]-dp[j-1][k-1]
			
			# If the count of flips is odd, then flip 0 to 1, let it be zero, 0^1=1
			if dp[j][k] % 2 != 0:
				matrix[j-1][k-1] = int(matrix[j-1][k-1]) ^ 1

# Function to update dp[][] matrix
# for each query
def queries_fxn(matrix, queries, dp):
	for q in queries:
		x1, y1, x2, y2 = q
		
		# Update the table
		dp[x1][y1] += 1
		dp[x2 + 1][y2 + 1] += 1
		dp[x1][y2 + 1] -= 1
		dp[x2 + 1][y1] -= 1
		
	modifyDP(matrix, dp)

# Driver Code
matrix = [[0, 0],[0,0]]
queries = [[1, 1, 2, 2], 
		[1, 1, 2, 2],[1, 1, 2, 2]]
# Initialize dp table
dp = [[0 for i in range(len(matrix[0])+2)] for j in range(len(matrix)+2)]

# Function call
queries_fxn(matrix, queries,dp)
print(matrix)
