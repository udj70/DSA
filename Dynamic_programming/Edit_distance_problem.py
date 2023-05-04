#task- Given- two strings, find min operation(replace, insert, delete) to convert S1 to S2
#approach 1- start from last char, if they are same, then no operation, make recursive call in i-1 and j-1
#        else 3 scenarios- min(insert in first make Recur call on i,j-1, delete in first make call on i-1,j, 
#                               replace in first String make Recur on i-1,j-1)

# approach2 - will do same thing with a dp (m X n)

def edit_distance(S1,S2):
    #  covert S1 --> S2
    m=len(S1)
    n=len(S2)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for j in range(n+1):
        dp[0][j]=j
    for i in range(m+1):
        dp[i][0]=i
    for i in range(1, m+1):
        for j in range(1, n+1):
            if S1[i-1] == S2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1+min(dp[i-1][j] , dp[i][j-1], dp[i-1][j-1])
    return dp[m-1][n-1]

#note whenever we observe current row is filled by prev row i.e dp[i-1], so use prev and current array
# and space will be reduced to O(n)
# just replace dp[i-1] with prev, and dp[i] with curr in old code.
# after every row just assign prev=curr
def edit_distance_On_space(S1,S2):
     #  covert S1 --> S2
    m=len(S1)
    n=len(S2)
    prev=[0 for _ in range(n+1)]
    curr=[0 for _ in range(n+1)]
    for j in range(n+1):
        prev[j]=j
    
    for i in range(1,m+1):
        for j in range(n+1):
            if j==0:
                curr[j]=i
            if S1[i-1] == S2[j-1]:
                curr[j] = prev[j-1]
            else:
                curr[j] = 1+min(prev[j] , curr[j-1], prev[j-1])
        prev=curr[:]
    return prev[n]


S1="abedf"
S2="kef"
print(edit_distance(S1,S2))
print(edit_distance_On_space(S1,S2))