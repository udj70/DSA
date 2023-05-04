#bottom up approach
def minsumpath(A):
    #make a 1 D array to store result from lowest row
    memo=[None]*len(A)
    n=len(A)-1
    #result of Bottom row
    for i in range(len(A[n])):
        memo[i]=A[n][i]
    #calculation of remaining rows in bottom up fashion
    for i in range(len(A)-2,-1,-1):
        for j in range(len(A[i])):
            memo[j]=A[i][j]+min(memo[j],memo[j+1])

    #return top element weight
    return memo[0]


A=[[2],
[3,9],
[1,6,7]]
print(minsumpath(A))             

