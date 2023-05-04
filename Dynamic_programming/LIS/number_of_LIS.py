# task- Give Integer array, find number of LIS that can be formed
# approach same as LIS, just slight change
def number_of_lis(arr):
    dp=[1]*len(arr)
    counts=[1]*len(arr)

    for i in range(len(arr)):
        for j in range(i-1,-1,-1):
            if arr[i]>arr[j]:
                if dp[j]+1>dp[i]:
                    dp[i]=dp[j]+1
                    counts[i] = counts[j]
                else:
                    counts[i]+=counts[j]
    mx=max(dp)
    ans=0
    for i in range(len(arr)):
        if dp[i]==mx:
            ans+=counts[i]
    print(counts)
    return ans

arr=[50, 9, 8, 7, 40, 80, 90]
print(number_of_lis(arr))

