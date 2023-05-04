#multiplication cost of matrix with dimensions a*b and b*c is a*b*c
def MCM(matrix,i,j):
    #base condition
    #if i==j then there is single matrix and its cost will be 0
    # if i>j i.e. no matrix hence cost zero
    if i>=j:
        return 0
    # initialize minimum cost of multiplication  of this partition to maximum    
    mn=float('inf')
    # traverse k from i to j
    # and calculate for each new partitions created i.e. i to k and k+1 to j
    for k in range(i,j):
        #in answers returned by two resursive calss add current cost also i.e. mat[i-1]*mat[k]*mat[j]
        temp=matrix[i-1]*matrix[k]*matrix[j] + MCM(matrix,i,k)+MCM(matrix,k+1,j)
        mn=min(mn,temp)
    return mn    
matrix=[10,20,30,20,30,50,20]
#call MCM with i=1(every matrix[i] represent matrix[i-1]*matrix[i] matrix dimensions ) and j=last element
ans=MCM(matrix,1,len(matrix)-1)
print(ans)




# tabulation

def MCM_dp(matrix):
    n=len(matrix)
    dp=[[0 for _ in range(n)] for _ in range(n)]
    # follow the recursion in reverse order, in top down, i was moving from 1 to n-1, in tabulation it will move from n-1 to 1
    for i  in range(n-1,0,-1):
        for j in range(i+1,n):
                # initialize minimum cost of multiplication  of this partition to maximum    
                mn=float('inf')
                # traverse k from i to j
                # and calculate for each new partitions created i.e. i to k and k+1 to j
                for k in range(i,j):
                    #in answers returned by two resursive calss add current cost also i.e. mat[i-1]*mat[k]*mat[j]
                    temp=matrix[i-1]*matrix[k]*matrix[j] + dp[i][k] + dp[k+1][j]
                    mn=min(mn,temp)
                dp[i][j]=mn
    return dp[1][n-1]    

matrix=[10,20,30,20,30,50,20]
print(MCM_dp(matrix))