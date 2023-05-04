#task- Write a solution to a problem in which we have to find no of 
# ways to reach nth stair with the use of 1,2,3 jumps only
#recursive solution-


'''
def countways(n):
    if n==1 or n==0:
        return 1
    elif n==2:
        return 2
    else:
        return countways(n-1)+countways(n-2)+countways(n-3)
'''
#DP solution
def countways(n):
    memo=[0]*(n+1)
    memo[0]=1
    memo[1]=1
    memo[2]=2
    for i in range(3,n+1):
         memo[i]=memo[i-1]+memo[i-2]+memo[i-3]
    return memo[n]
n=4
print(countways(n))    



















      
