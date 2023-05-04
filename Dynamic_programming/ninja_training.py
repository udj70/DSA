'''
Ninja is planing this ‘N’ days-long training schedule. Each day, he can perform any one of these three activities. (Running, Fighting Practice or Learning New Moves). Each activity has some merit points on each day. As Ninja has to improve all his skills, he can’t do the same activity in two consecutive days. Can you help Ninja find out the maximum merit points Ninja can earn?
You are given a 2D array of size N*3 ‘POINTS’ with the points corresponding to each day and activity. Your task is to calculate the maximum number of merit points that Ninja can earn.
For Example
If the given ‘POINTS’ array is [[1,2,5], [3 ,1 ,1] ,[3,3,3] ],the answer will be 11 as 5 + 3 + 3.

'''
# approach 1- recursive

def ninja_training_recur(days,d,last):
    if d==0:
        maxi=0
        for i in range(2):
            if i !=last:
                maxi=max(maxi,days[0][i])
        return maxi
    maxi=0
    for i in range(2):
        if i !=last:
            maxi=max(maxi,days[d][i]+ninja_training_recur(days,d-1,i))
    return maxi
days=[[1,2,5], [3 ,1 ,1] ,[3,3,3] ]
d=len(days)-1
print("recursion-",max(days[d][0]+ninja_training_recur(days,d,0),days[d][1]+ninja_training_recur(days,d,1),days[d][2]+ninja_training_recur(days,d,2)))


# approach 2- recursion + memoisation

def ninja_training_memo(days,d,last,dp):
    if d==0:
        maxi=0
        for i in range(2):
            if i !=last:
                maxi=max(maxi,days[0][i])
        return maxi
    
    if dp[d][last]!=-1:
        return dp[d][last]

    maxi=0
    for i in range(2):
        if i !=last:
            maxi=max(maxi,days[d][i]+ninja_training_memo(days,d-1,i,dp))
    dp[d][last] = maxi
    return maxi
days=[[1,2,5], [3 ,1 ,1] ,[3,3,3] ]
d=len(days)-1
dp=[[-1 for _ in range(3)] for _ in range(len(days))]
print("memoisation-",max(days[d][0]+ninja_training_memo(days,d,0,dp),days[d][1]+ninja_training_memo(days,d,1,dp),days[d][2]+ninja_training_memo(days,d,2,dp)))

# appraoch 3- tabulation

def ninja_training_tabulation(days):
    dp=[[0 for _ in range(3)] for _ in range(len(days)) ]
    dp[0][0]=max(days[0][1],days[0][2])
    dp[0][1]=max(days[0][0],days[0][2])
    dp[0][2]=max(days[0][0],days[0][1])
    for i in range(1,len(days)):
        # for all possible last value
        for last in range(3):
            # calculate answer for remainig two last
            maxi=0
            for task in range(3):
                if task!=last:
                    maxi=max(maxi,days[i][task]+dp[i-1][task])
            dp[i][last]=maxi
    return max(dp[len(days)-1][0],dp[len(days)-1][1],dp[len(days)-1][2])
days=[[1,2,5], [3 ,1 ,1] ,[3,3,3] ]
print("tabulation",ninja_training_tabulation(days))


# approach 4- tabulation+space optimisation