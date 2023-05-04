# task- Given a integer array, find longest bitonic subsequence such that it might be increasing or decreasing or both at the time

# approach - same as LIS, with slight change, i.e get LIS from left and right, merge answers and subtract common element, now calculate max among all

def LBS_dp(arr):
    # LIS from left
    dp1=[1]*len(arr) # intially LIS is 1

    for i in range(len(arr)):
        for j in range(i-1,-1,-1):
            if arr[i]>arr[j]:
                if dp1[j]+1>dp1[i]:
                    dp1[i]=dp1[j]+1
                    
                # dp[i] = max(dp[i],dp[j]+1)
    
    # LIS from right
    dp2 = [1] * len(arr)

    for i in range(len(arr)-1,-1,-1):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                if dp2[j]+1>dp2[i]:
                    dp2[i]=dp2[j]+1
                    
                # dp[i] = max(dp[i],dp[j]+1)

    # merge answer from dp1 and dp2
    mx=0
    for i in range(len(arr)):
        mx=max(mx,dp1[i]+dp2[i]-1)

    return mx 
arr=[50, 9, 8, 7, 40, 80,90]

print(LBS_dp(arr))
