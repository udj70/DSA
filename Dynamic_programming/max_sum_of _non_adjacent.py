# task- given array, find max sum subseqence with no adjancent element

#refer striver for all these solution
# approach 1- recursive
def max_sum_subsequence_recursive(arr,index):
    if index==0:
        return arr[index]
    if index<0:
        return 0

    pick=max_sum_subsequence_recursive(arr,index-2)+arr[index]
    not_pick=max_sum_subsequence_recursive(arr,index-1)
    return max(pick,not_pick)
arr=[2,1,4,9]
print("recursive",max_sum_subsequence_recursive(arr,len(arr)-1))

# approach 2- recursion+memoisation
def max_sum_subsequence_memo(arr,index,dp):
    if index==0:
        return arr[index]
    if index<0:
        return 0
    
    if dp[index]!=-1:
        return dp[index]

    pick=max_sum_subsequence_memo(arr,index-2,dp)+arr[index]
    not_pick=max_sum_subsequence_memo(arr,index-1,dp)

    dp[index]=max(pick,not_pick)
    return dp[index]
    
arr=[2,1,4,9]
dp=[-1]*len(arr)
print("recursive+memoisation",max_sum_subsequence_memo(arr,len(arr)-1,dp))

# approach 3 -tabulation (bottom up)

def max_sum_subsequence_tabulation(arr):
    dp=[0]*len(arr)
    dp[0]=arr[0]
    for index in range(1,len(arr)):
        
        pick=arr[index]
        not_pick=float('-inf')
        if index-2>=0:
            pick+=dp[index-2]
        
        not_pick=dp[index-1]
        dp[index]=max(pick,not_pick)
    return dp[len(arr)-1]
arr=[2,1,4,9]
print("tabulation-",max_sum_subsequence_tabulation(arr))

# approach 4- tabulation+space optimisation

def max_sum_subsequence_tabulation_opt(arr):
    
    prev=arr[0]
    prev2=0
    curr=0
    for index in range(1,len(arr)):
        
        pick=arr[index]
        not_pick=float('-inf')
        if index-2>=0:
            pick+=prev2
        not_pick=prev
        
        curr=max(pick,not_pick)
        prev2=prev
        prev=curr
    return prev
arr=[2,1,4,9]
print("tabulation+ space optimisation-",max_sum_subsequence_tabulation_opt(arr))