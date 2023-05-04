#recursive solution
def IsSubsetSum_r(arr,n,s):
    if s>0 and n==0:
        return False
    elif s==0:
        return True
    elif arr[n-1]>s:
        return IsSubsetSum_r(arr,n-1,s)
            
    else:
        return IsSubsetSum_r(arr,n-1,s-arr[n-1]) or IsSubsetSum_r(arr,n-1,s)
arr=[1,2,2,3,4]
print(IsSubsetSum_r(arr,len(arr),3))  

#dp solution
def IsSubsetSum_dp(arr,s):
    dp=[[False for _ in range(s+1)] for _ in range(len(arr)+1)]
    for i in range(len(arr)+1):
        dp[i][0]=True
    for i in range(1,len(arr)+1):
        for j in range(1,s+1):
            if arr[i-1]>j:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j] or dp[i-1][j-arr[i-1]]  
    print(dp)            
    #logic for generating minimum subsets difference from last row of dp table,just need to pass sum of arr as sum parameter in function
    '''lis=[]
    for i in range((s+1)//2+1):
        if dp[len(arr)][i]:
            lis.append(i)
    print(s-2*lis[-1])   '''     
    return dp[len(arr)][s]
ar=[1,2,3,4,5]
print(IsSubsetSum_dp(ar,5))    
