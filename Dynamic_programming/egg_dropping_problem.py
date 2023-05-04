#task-> Given E eggs, F floors , find the minimum number of attempts required to find critical floor from which egg will break.
#approach-> traverse each floor and at each floor there will be two case-
#               1. either egg will break, then critical floor will lie in f-1 floors
#               2. or egg will not break, then critical floor will lie in f+1 floors
# check each floor one by one and consider both scenario, capture maximum of both and then calculate min of all maximum attempts
# return 1+ min attempts(current attempt will add up in answer)

#sol-1
# top down recursive approach TC=exponential




def number_of_attempts(floors,eggs):
    # if floors is zero, then num of attempts will be zero
    # if floors i one then attempts will 1 only
    if floors==0 or floors==1:
        return floors
    # if egg is one then number attempts will be equal to floors
    if eggs==1:
        return floors
    mn=float('inf')    
    # check in each floors
    for i in range(1,floors+1):
        #if egg breaks
        egg_break=number_of_attempts(i-1,eggs-1)
        not_break=number_of_attempts(floors-i,eggs)
        temp=max(egg_break,not_break)
        mn=min(temp,mn)
    #return minimum attempts + 1(cuurent attempt)
    return mn+1    
f=10
e=2 
print(number_of_attempts(f,e))   

# sol 2
# topdown memoized
# just create dp of size floors+1 and eggs+1
# and store result in dp[eggs][fllors] before returning

#sol 3
# bottom dp

def number_of_attempts_dp(floors,eggs):
    dp=[[None for _ in range(floors+1)] for _ in range(eggs+1)]
    #first row will have none because with 0 eggs no attempts is possible
    for i in range(1,eggs+1):
        #when floors is 0 then attempts will be 0
        dp[i][0]=0
    for i in range(1,floors+1):
        #when number of eggs is 1 then number of attempts will be equals to number of floors
        dp[1][i]=i
    for i in range(1,eggs+1):
        #when floor is one then number of attempt will be one
        dp[i][1]=1        
    for i in range(2,eggs+1):
        for j in range(2,floors+1):
            mn=float('inf')
            for k in range(1,j+1):
                #if egg break at k floor, then search in k-1 floors, with i-1 eggs, 
                #if not break then search in j-k floors, with i eggs
                # cal max of both scenario
                # and save min of all max
                temp=max(dp[i-1][k-1],dp[i][j-k])
                mn=min(temp,mn) 
            # save min plus 1(current attempt)
            dp[i][j]=mn+1  
    return dp[eggs][floors]

f=10
e=2
print(number_of_attempts_dp(f,e))