def maxsumpath(A):
    n=len(A)-1
    memo=[None]*len(A)
    for j in range(len(A[n])):
        memo[j]=A[n][j]
    for i in range(n-1,-1,-1):
        for j in range(len(A[i])):

            memo[j]=A[i][j]+max(memo[j],memo[j+1])
    return memo[0]            









A=[[2],
[3,9],
[1,6,7]]
print(maxsumpath(A))             
