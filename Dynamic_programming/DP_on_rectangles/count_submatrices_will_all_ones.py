# task- Given a matrix with one and zeroes, calculate count of all square submatrices of all ones can be formed 
# approach 1- start at each ones and expand it downards, count square matrices
# approach 2- create dp grid, observe a pattern, standing at any particular cell, we have to calculate how many submatrices can be formed ending with current cell(if cell is 1)
#             to do this, submatrices ending at i,j is min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
# refer striver

def calculate_submatrices(grid):
    
    dp=[[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

    # initalize 0 row and colomn with 1 with it contains 1 else 0

    for i in range(len(grid)):
        dp[i][0] = grid[i][0]
    for j in range(len(grid[0])):
        dp[0][j] = grid[0][j]
    
    for i in range(1,len(grid)):
        for j in range(1,len(grid[0])):
            if grid[i][j] == 1:
                dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
            else:
                dp[i][j]=0
    return sum([sum(d) for d in dp])

grid=[[1,1],[1,1]] # 5
print(calculate_submatrices(grid))
    
