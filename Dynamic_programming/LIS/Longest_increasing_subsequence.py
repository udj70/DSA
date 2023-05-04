'''from itertools import permutations,combinations
lis=[1,2,3,4]
x=permutations(lis,2)
for i in x:
    print(i)
print("comb")
y=combinations(lis,2)
for i in y:
    print(i)
'''

# recurisve
def LIS(arr,i,prev):
    if i==len(arr):
        return 0

    if prev==-1 or arr[i]>arr[prev]:
        return max(1+LIS(arr,i+1,i),LIS(arr,i+1,prev))
    else:
        return LIS(arr,i+1,prev)
arr=[50, 9, 8, 7, 40, 80,90]
print(LIS(arr,0,-1))

# recursive + memo
def LIS_memo(arr,i,prev,dp):
    if i==len(arr):
        return 0
    # because we are starting our prev from -1, while storing we have to make cordinate change to prev+1
    if dp[i][prev+1]!=-1:
        return dp[i][prev+1]
    if prev==-1 or arr[i]>arr[prev]:
        dp[i][prev+1] = max(1+LIS_memo(arr,i+1,i,dp),LIS_memo(arr,i+1,prev,dp))
    else:
        dp[i][prev+1] = LIS_memo(arr,i+1,prev,dp)
    return dp[i][prev+1]
arr=[50, 9, 8, 7, 40, 80,90]
dp=[[-1 for _ in range(len(arr)+1)] for _ in range(len(arr)+1)]
print(LIS_memo(arr,0,-1,dp))

# tabulation

def LIS_dp(arr):
    dp=[[0 for _ in range(len(arr)+1)] for _ in range(len(arr)+1)]
    for i in range(len(arr)-1,-1,-1):
        for prev in range(i-1,-2,-1):
            if prev==-1 or arr[i]>arr[prev]:
                dp[i][prev+1] = max(1+dp[i+1][i+1],dp[i+1][prev+1])
            else:
                dp[i][prev+1] = dp[i+1][prev+1]
    return dp[0][-1+1]
arr=[50, 9, 8, 7, 40, 80,90]

print(LIS_dp(arr))

# alternate dp
def LIS_dp_alternate(arr):
    dp=[1]*len(arr)
    for i in range(len(arr)):
        for j in range(i-1,-1,-1):
            if arr[i]>arr[j]:
                dp[i] = max(dp[i],dp[j]+1)
    return max(dp)

arr=[50, 9, 8, 7, 40, 80,90]

print(LIS_dp_alternate(arr))


# print LIS

def LIS_dp_alternate_print(arr):
    dp=[1]*len(arr) # intially LIS is 1

    # to store index of prev of current cell, for backtracking purpose
    idx_hash=[i for i in range(len(arr))]

    for i in range(len(arr)):
        for j in range(i-1,-1,-1):
            if arr[i]>arr[j]:
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
    print()
    return 
arr=[50, 9, 8, 7, 40, 80,90]

LIS_dp_alternate_print(arr)

# LIS nlogn approach
def binary_search(arr,n):
    start=0
    end=len(arr)-1
    idx=-1
    while(start<=end):
        mid= start + (end-start)//2
        if arr[mid]>=n:
            idx=mid
            end=mid-1
        else:
            start=mid+1 
    return idx

def LIS_logn(arr):
    temp=[]
    temp.append(arr[0])
    for i in range(1,len(arr)):
        if not len(temp) or arr[i]>temp[-1]:
            temp.append(arr[i])
        else:
            index=binary_search(temp,arr[i]) # it will return index of element just greater that arr[i]
            temp[index]=arr[i]
    return len(temp)

arr=[50, 9, 8, 7, 40, 80,90]

print(LIS_logn(arr))
    
