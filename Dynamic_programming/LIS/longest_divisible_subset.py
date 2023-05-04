# task- given integer array, find subset such that all number are divisible by any of the other number in array
# approach - same as LIS
def LDS_dp_alternate_print(arr):
    dp=[1]*len(arr) # intially LIS is 1
    arr.sort()
    # to store index of prev of current cell, for backtracking purpose
    idx_hash=[i for i in range(len(arr))]

    for i in range(len(arr)):
        for j in range(i-1,-1,-1):
            if arr[i]%arr[j]==0 or arr[j]%arr[i]==0:
                if dp[j]+1>dp[i]:
                    dp[i]=dp[j]+1
                    idx_hash[i]=j
                # dp[i] = max(dp[i],dp[j]+1)
    
    idx=dp.index(max(dp))
    #print(idx_hash)
    # start backtracking from index
    count=0
    while(count<max(dp) and idx>=0):
        print(arr[idx],end=" ")
        idx=idx_hash[idx]
        count+=1
    print("LDS", max(dp))
    return 
arr=[2, 5, 1, 4, 7, 8, 16]

LDS_dp_alternate_print(arr)