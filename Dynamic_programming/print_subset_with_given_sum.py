#it will print any one of the subset not all
def print_subset_with_sum(arr,s):

    dp=[[False for _ in range(s+1)] for _ in range(len(arr)+1)]
    for i in range(len(arr)+1):
        dp[i][0]=True
    for i in range(1,len(arr)+1):
        for j in range(1,s+1):
            if arr[i-1]<=j:
                dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    #print(dp)
    if dp[len(arr)][s]:  
        j=s
        i=len(arr)
        while(j>0):
            #current element is not included
            if dp[i-1][j]:
                i=i-1
            # if current element is included            
            elif j-arr[i-1]>=0:
                print(arr[i-1])
                
                j=j-arr[i-1]
                i=i-1
            else:
                break
    print_all_posibble_subset(arr,dp,len(arr),s,[]) #non working function, will check
#non working logic
def print_all_posibble_subset(arr,dp,i,j,subset):
    if j<0:
        return
    if i<=0:
        return
    if j==0:
        print(subset)
    if dp[i-1][j]:
        print_all_posibble_subset(arr,dp,i-1,j,subset)
    if dp[i-1][j-arr[i-1]]:
        subset.append(arr[i-1])
        print_all_posibble_subset(arr,dp,i-1,j-arr[i-1],subset)
        subset.pop()
    


arr=[2,3,5,6,8,10]
s=11
print_subset_with_sum(arr,s)